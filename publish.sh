#!/bin/bash

# Manual PyPI Publishing Script for abov3-ai
# This script builds and publishes the package to PyPI

set -e

echo "Publishing abov3-ai Python SDK to PyPI..."

# Check if PYPI_API_TOKEN is set
if [ -z "$PYPI_API_TOKEN" ]; then
    echo "Error: PYPI_API_TOKEN environment variable is not set"
    echo "Please set it with: export PYPI_API_TOKEN=your_token_here"
    exit 1
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist/ build/ *.egg-info src/*.egg-info

# Install required tools
echo "Installing build tools..."
pip install --upgrade pip build twine

# Build the package
echo "Building the package..."
python -m build

# Check the package
echo "Checking package with twine..."
twine check dist/*

# Upload to PyPI
echo "Uploading to PyPI..."
TWINE_USERNAME=__token__ TWINE_PASSWORD=$PYPI_API_TOKEN twine upload dist/*

echo "Successfully published to PyPI!"
echo "View at: https://pypi.org/project/abov3-ai/"