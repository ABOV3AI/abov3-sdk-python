# Publishing Guide for ABOV3 Python SDK

This guide explains how to publish the ABOV3 Python SDK to PyPI and Test PyPI.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Publishing Methods](#publishing-methods)
- [Setting Up PyPI Publishing](#setting-up-pypi-publishing)
- [Setting Up Test PyPI Publishing](#setting-up-test-pypi-publishing)
- [Publishing Workflow](#publishing-workflow)
- [Version Management](#version-management)
- [Troubleshooting](#troubleshooting)

## Prerequisites

Before publishing, ensure you have:
1. A [PyPI account](https://pypi.org/account/register/)
2. A [Test PyPI account](https://test.pypi.org/account/register/) (optional, for testing)
3. Repository admin access to [ABOV3AI/abov3-sdk-python](https://github.com/ABOV3AI/abov3-sdk-python)

## Publishing Methods

The SDK supports two authentication methods for publishing:

### 1. Trusted Publishing (Recommended)
- Uses OpenID Connect (OIDC) for authentication
- No API tokens needed
- More secure - tokens are short-lived and scoped
- Configured directly on PyPI/Test PyPI

### 2. API Token Authentication
- Traditional method using long-lived tokens
- Stored as GitHub secrets
- Fallback option if trusted publishing isn't configured

## Setting Up PyPI Publishing

### Option 1: Trusted Publishing Setup

1. **Log in to PyPI**: https://pypi.org/manage/account/

2. **Navigate to Publishing**:
   - Go to "Publishing" → "Add a new pending publisher"

3. **Configure the Publisher**:
   ```
   PyPI Project Name: abov3-ai
   Repository owner: ABOV3AI
   Repository name: abov3-sdk-python
   Workflow name: publish.yml
   Environment name: pypi
   ```

4. **Save the configuration**

### Option 2: API Token Setup

1. **Create an API Token**:
   - Go to https://pypi.org/manage/account/token/
   - Create a new token (optionally scoped to `abov3-ai` project)
   - Copy the token (starts with `pypi-`)

2. **Add to GitHub Secrets**:
   - Go to https://github.com/ABOV3AI/abov3-sdk-python/settings/secrets/actions
   - Click "New repository secret"
   - Name: `PYPI_API_TOKEN`
   - Value: Your PyPI token
   - Click "Add secret"

## Setting Up Test PyPI Publishing

### Option 1: Trusted Publishing Setup

1. **Log in to Test PyPI**: https://test.pypi.org/manage/account/

2. **Navigate to Publishing**:
   - Go to "Publishing" → "Add a new pending publisher"

3. **Configure the Publisher**:
   ```
   PyPI Project Name: abov3-ai
   Repository owner: ABOV3AI
   Repository name: abov3-sdk-python
   Workflow name: publish.yml
   Environment name: test-pypi
   ```

4. **Save the configuration**

### Option 2: API Token Setup

1. **Create a Test PyPI Token**:
   - Go to https://test.pypi.org/manage/account/token/
   - Create a new token
   - Copy the token

2. **Add to GitHub Secrets**:
   - Go to https://github.com/ABOV3AI/abov3-sdk-python/settings/secrets/actions
   - Click "New repository secret"
   - Name: `TEST_PYPI_API_TOKEN`
   - Value: Your Test PyPI token
   - Click "Add secret"

## Publishing Workflow

### Automatic Publishing

The SDK automatically publishes to PyPI when:
- A new GitHub release is created
- A version tag is pushed (e.g., `v0.1.0`)

```bash
# Create and push a version tag
git tag v0.1.0
git push origin v0.1.0
```

### Manual Publishing

1. **Go to Actions**: https://github.com/ABOV3AI/abov3-sdk-python/actions

2. **Select "Publish to PyPI" workflow**

3. **Click "Run workflow"**

4. **Choose options**:
   - Branch: `main`
   - Version: Optional (e.g., `0.1.0`)

5. **Click "Run workflow"**

### Testing with Test PyPI

Before publishing to production PyPI:

1. **Run the workflow manually** (as above)
2. **Check Test PyPI**: https://test.pypi.org/project/abov3-ai/
3. **Test installation**:
   ```bash
   pip install -i https://test.pypi.org/simple/ abov3-ai
   ```

## Version Management

### Updating Version

The version is defined in `pyproject.toml`:

```toml
[project]
name = "abov3-ai"
version = "0.1.0"  # Update this
```

### Version Format

Follow [Semantic Versioning](https://semver.org/):
- **MAJOR.MINOR.PATCH** (e.g., `1.2.3`)
- **MAJOR**: Breaking changes
- **MINOR**: New features, backward compatible
- **PATCH**: Bug fixes, backward compatible

### Pre-release Versions

For testing and pre-releases:
- Alpha: `0.1.0a1`
- Beta: `0.1.0b1`
- Release Candidate: `0.1.0rc1`

## Troubleshooting

### Common Issues

#### 1. Trusted Publishing Error
**Error**: `invalid-publisher: valid token, but no corresponding publisher`

**Solution**:
- Ensure the publisher configuration on PyPI matches exactly:
  - Repository: `ABOV3AI/abov3-sdk-python`
  - Workflow: `publish.yml`
  - Environment: `pypi` or `test-pypi`

#### 2. Permission Denied
**Error**: `403 Forbidden`

**Solution**:
- Check API token is valid and not expired
- Ensure token has upload permissions
- For project-scoped tokens, ensure project name matches

#### 3. Version Already Exists
**Error**: `400 File already exists`

**Solution**:
- Increment version in `pyproject.toml`
- Delete the existing version (if on Test PyPI)
- The workflow has `skip-existing: true` to prevent failures

#### 4. OIDC Token Error
**Error**: `missing or insufficient OIDC token permissions`

**Solution**:
- Workflow already has correct permissions set
- Ensure you're using the latest workflow from `main` branch

### Workflow Permissions

The workflow requires these permissions (already configured):
```yaml
permissions:
  id-token: write  # For trusted publishing
  contents: read   # To access repository
```

### Testing Locally

To test the package build locally:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Check the package
twine check dist/*

# Upload to Test PyPI (manual)
twine upload --repository testpypi dist/*
```

## Security Best Practices

1. **Prefer Trusted Publishing** over API tokens
2. **Use project-scoped tokens** when using API tokens
3. **Enable 2FA** on PyPI and GitHub accounts
4. **Rotate tokens regularly** if using API tokens
5. **Never commit tokens** to the repository
6. **Use GitHub secrets** for sensitive data

## Package URLs

Once published, the package will be available at:

- **PyPI**: https://pypi.org/project/abov3-ai/
- **Test PyPI**: https://test.pypi.org/project/abov3-ai/
- **Installation**: `pip install abov3-ai`

## GitHub Environments

The workflow uses GitHub environments for deployment protection:

- **`pypi`**: Production PyPI publishing
- **`test-pypi`**: Test PyPI publishing

You can add additional protection rules in:
Settings → Environments → [environment name] → Protection rules

## Support

For issues or questions:
- **GitHub Issues**: https://github.com/ABOV3AI/abov3-sdk-python/issues
- **ABOV3 Support**: support@abov3.ai
- **Documentation**: https://www.abov3.ai/docs