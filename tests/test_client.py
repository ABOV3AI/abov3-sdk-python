"""Tests for ABOV3 client"""

import os
import pytest
from unittest.mock import patch, MagicMock

from abov3 import Abov3Client
from abov3.exceptions import Abov3Error


class TestAbov3Client:
    """Test ABOV3 client initialization and basic operations."""

    def test_client_requires_api_key(self):
        """Test that client raises error when no API key is provided."""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(Abov3Error) as exc_info:
                Abov3Client()
            assert "API key is required" in str(exc_info.value)

    def test_client_uses_env_api_key(self):
        """Test that client uses API key from environment variable."""
        with patch.dict(os.environ, {"ABOV3_API_KEY": "test-key"}):
            client = Abov3Client()
            assert client.api_key == "test-key"

    def test_client_explicit_api_key(self):
        """Test that explicit API key overrides environment variable."""
        with patch.dict(os.environ, {"ABOV3_API_KEY": "env-key"}):
            client = Abov3Client(api_key="explicit-key")
            assert client.api_key == "explicit-key"

    def test_client_default_base_url(self):
        """Test that client uses default base URL."""
        client = Abov3Client(api_key="test-key")
        assert client.base_url == "https://api.abov3.ai"

    def test_client_env_base_url(self):
        """Test that client uses base URL from environment."""
        with patch.dict(os.environ, {"ABOV3_BASE_URL": "http://localhost:8080"}):
            client = Abov3Client(api_key="test-key")
            assert client.base_url == "http://localhost:8080"

    def test_client_explicit_base_url(self):
        """Test that explicit base URL overrides environment variable."""
        with patch.dict(os.environ, {"ABOV3_BASE_URL": "http://env-url"}):
            client = Abov3Client(api_key="test-key", base_url="http://explicit-url")
            assert client.base_url == "http://explicit-url"

    @pytest.mark.asyncio
    async def test_client_context_manager(self):
        """Test that client works as async context manager."""
        client = Abov3Client(api_key="test-key")

        # Mock the close method
        close_mock = MagicMock()
        client.close = close_mock

        async with client as c:
            assert c == client

        close_mock.assert_called_once()