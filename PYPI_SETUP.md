# PyPI Publishing Setup for abov3-ai

This document explains how to publish the abov3-ai Python SDK to PyPI.

## Package Information
- **Package Name**: abov3-ai
- **PyPI URL**: https://pypi.org/project/abov3-ai/
- **GitHub Repo**: https://github.com/ABOV3AI/abov3-sdk-python

## Setup Requirements

### 1. PyPI Account Setup
1. Create an account at https://pypi.org if you don't have one
2. Generate an API token:
   - Go to https://pypi.org/manage/account/token/
   - Create a new token with scope "Entire account" or project-specific
   - Save the token securely (starts with `pypi-`)

### 2. GitHub Repository Setup

#### Add PyPI Token as GitHub Secret
1. Go to https://github.com/ABOV3AI/abov3-sdk-python/settings/secrets/actions
2. Click "New repository secret"
3. Name: `PYPI_API_TOKEN`
4. Value: Your PyPI API token (including the `pypi-` prefix)
5. Click "Add secret"

## Publishing Methods

### Method 1: Automated Publishing via GitHub Actions

The repository includes a GitHub Actions workflow that automatically publishes to PyPI.

#### Trigger via GitHub Release:
1. Go to https://github.com/ABOV3AI/abov3-sdk-python/releases/new
2. Create a new release with a version tag (e.g., `v0.1.5`)
3. The workflow will automatically build and publish to PyPI

#### Trigger Manually:
1. Go to https://github.com/ABOV3AI/abov3-sdk-python/actions/workflows/publish-pypi.yml
2. Click "Run workflow"
3. Enter the version number (e.g., `0.1.5`)
4. Click "Run workflow"

### Method 2: Manual Publishing (Local)

1. Clone the repository:
   ```bash
   git clone https://github.com/ABOV3AI/abov3-sdk-python.git
   cd abov3-sdk-python
   ```

2. Set your PyPI API token:
   ```bash
   export PYPI_API_TOKEN=your_pypi_token_here
   ```

3. Run the publish script:
   ```bash
   ./publish.sh
   ```

### Method 3: Manual Commands

1. Install build tools:
   ```bash
   pip install --upgrade pip build twine
   ```

2. Clean previous builds:
   ```bash
   rm -rf dist/ build/ *.egg-info
   ```

3. Build the package:
   ```bash
   python -m build
   ```

4. Check the package:
   ```bash
   twine check dist/*
   ```

5. Upload to PyPI:
   ```bash
   TWINE_USERNAME=__token__ TWINE_PASSWORD=your_pypi_token twine upload dist/*
   ```

## Version Management

The package version is defined in `pyproject.toml`:
```toml
[project]
name = "abov3-ai"
version = "0.1.4"  # Update this for new releases
```

## Testing the Published Package

After publishing, test the installation:

```bash
pip install abov3-ai --upgrade
python -c "import abov3; print(abov3.__version__)"
```

## Troubleshooting

### Common Issues:

1. **Authentication Failed**
   - Ensure your API token is correct and includes the `pypi-` prefix
   - Check that the token has the correct scope

2. **Version Already Exists**
   - PyPI doesn't allow re-uploading the same version
   - Increment the version in `pyproject.toml`

3. **Package Name Conflicts**
   - The package name `abov3-ai` is already registered
   - Only authorized users can upload to this package

## Support

For issues or questions:
- GitHub Issues: https://github.com/ABOV3AI/abov3-sdk-python/issues
- Email: support@abov3.ai