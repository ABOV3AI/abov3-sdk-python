# Release Process for abov3-ai Python SDK

## Automatic PyPI Publishing

The SDK is automatically published to PyPI when:

### 1. Creating a Git Tag (Recommended)
```bash
# Update version in pyproject.toml and src/abov3/__init__.py
# Commit changes
git add -A
git commit -m "chore: bump version to X.Y.Z"
git push origin main

# Create and push a version tag
git tag vX.Y.Z -m "Release version X.Y.Z"
git push origin vX.Y.Z
```

### 2. Creating a GitHub Release
- Go to GitHub repository → Releases → Draft a new release
- Create a tag in the format `vX.Y.Z`
- Add release notes
- Publish release

### 3. Manual Workflow Dispatch
- Go to Actions → "Publish to PyPI" workflow
- Click "Run workflow"
- Enter version number (optional)

## Version Update Checklist

Before creating a release, update the version in:
- [ ] `pyproject.toml` - `version = "X.Y.Z"`
- [ ] `src/abov3/__init__.py` - `__version__ = "X.Y.Z"`

## CI/CD Workflows

### CI Workflow (`ci.yml`)
- Runs on every push to main and PRs
- Tests Python 3.8-3.12 compatibility
- Runs linting (black, ruff, mypy)
- Executes test suite

### Publish Workflow (`publish.yml`)
- Triggered by tags starting with `v*`
- Builds Python package
- Publishes to PyPI using API token
- Optional Test PyPI publishing for testing

## Requirements

- **PYPI_API_TOKEN**: Must be set in repository secrets
- Version tag must start with 'v' (e.g., v0.1.3)
- Version in pyproject.toml should match tag version

## Troubleshooting

If publishing fails:
1. Check GitHub Actions logs
2. Verify PYPI_API_TOKEN is set correctly
3. Ensure version doesn't already exist on PyPI
4. Check that build dependencies are correct

## PyPI Package

- Package name: `abov3-ai`
- PyPI URL: https://pypi.org/project/abov3-ai/
- Install: `pip install abov3-ai`