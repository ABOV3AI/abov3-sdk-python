# ABOV3 Python SDK v0.1.11

Official Python SDK for ABOV3 AI - Genesis CodeForger Edition

---

## What's New in v0.1.11

### 🔄 Version Alignment
- Updated to align with ABOV3 Genesis CodeForger v0.1.6
- Synchronized with latest ABOV3 features and API changes

### 🐛 Bug Fixes
- Improved error handling for API timeouts
- Enhanced type hints for better IDE support

### 📚 Documentation
- Updated repository references to ABOV3AI organization
- Enhanced README with usage examples

---

## Installation

```bash
pip install abov3-ai==0.1.11
```

Or upgrade from previous version:

```bash
pip install --upgrade abov3-ai
```

---

## Quick Start

```python
from abov3 import Abov3Client

# Initialize client
client = Abov3Client(base_url="http://localhost:4096")

# List available sessions
sessions = await client.sessions.list()

# Create a new session
session = await client.sessions.create()

# Send a message
response = await client.chat.send(
    session_id=session.id,
    message="Help me write a Python function"
)
```

---

## Features

- ✨ **Async/await support** - Modern async Python patterns
- 🔒 **Type safety** - Full Pydantic model support
- 🔄 **Automatic retries** - Built-in retry logic for failed requests
- 📝 **Comprehensive types** - Full type hints for IDE support
- 🚀 **Streaming responses** - Real-time response streaming

---

## Requirements

- Python 3.8+
- httpx >= 0.24.0
- pydantic >= 2.0.0
- typing-extensions >= 4.5.0

---

## Documentation

- 📚 **ABOV3 Documentation**: https://www.abov3.ai/docs
- 🐍 **Python SDK Repository**: https://github.com/ABOV3AI/abov3-sdk-python
- 📦 **PyPI Package**: https://pypi.org/project/abov3-ai/

---

## Support

- 💬 **Issues**: https://github.com/ABOV3AI/abov3-sdk-python/issues
- 🏠 **Website**: https://www.abov3.ai
- 📧 **Email**: support@abov3.ai

---

**Author**: Fahad Ibn Omar Fajardo
**License**: MIT