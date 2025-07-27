"""
Integration tests for API endpoints
"""

import pytest
from fastapi.testclient import TestClient
from pytonator.main import app

client = TestClient(app)

class TestAPIIntegration:
    """Integration tests for API endpoints"""
    
    def test_full_api_flow(self):
        """Test complete API flow"""
        # Test health check
        health_response = client.get("/health")
        assert health_response.status_code == 200
        
        # Test info endpoint
        info_response = client.get("/api/v1/info")
        assert info_response.status_code == 200
        
        # Test status endpoint
        status_response = client.get("/api/v1/status")
        assert status_response.status_code == 200
        
        # Test echo endpoint
        echo_response = client.post("/api/v1/echo", json={"message": "Integration test"})
        assert echo_response.status_code == 200
    
    def test_api_documentation(self):
        """Test API documentation endpoints"""
        # Test OpenAPI docs
        docs_response = client.get("/docs")
        assert docs_response.status_code == 200
        
        # Test ReDoc
        redoc_response = client.get("/redoc")
        assert redoc_response.status_code == 200
```

```ini:pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = 
    --strict-markers
    --strict-config
    --verbose
    --tb=short
    --cov=pytonator
    --cov-report=term-missing
    --cov-report=html
    --cov-report=xml
markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow running tests
```

```toml:pyproject.toml
[build-system]
requires = ["setuptools>=61.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pytonator"
version = "0.1.0"
description = "A Python application for CI/CD demonstration"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
keywords = ["python", "fastapi", "ci-cd", "demo"]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.11",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.3",
    "pytest-cov>=4.1.0",
    "pytest-asyncio>=0.21.1",
    "pytest-mock>=3.12.0",
    "factory-boy>=3.3.0",
    "flake8>=6.1.0",
    "black>=23.11.0",
    "isort>=5.12.0",
    "mypy>=1.7.1",
    "types-requests>=2.31.0.10",
    "types-PyYAML>=6.0.12.12",
    "sphinx>=7.2.6",
    "sphinx-rtd-theme>=1.3.0",
]

[tool.black]
line-length = 88
target-version = ['py311']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

[tool.isort]
profile = "black"
multi_line_output = 3
line_length = 88
known_first_party = ["pytonator"]

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
disallow_untyped_decorators = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
warn_unreachable = true
strict_equality = true

[[tool.mypy.overrides]]
module = [
    "tests.*",
]
disallow_untyped_defs = false
disallow_incomplete_defs = false
```

```markdown:README.md
# Pytonator

A Python application for CI/CD demonstration with comprehensive testing and security scanning.

## Features

- FastAPI-based REST API
- Comprehensive test suite (unit and integration tests)
- Security scanning with Trivy
- Containerized deployment with Kaniko
- GitLab CI/CD pipeline with proper stage naming
- Code quality tools (Black, isort, flake8, mypy)

## Quick Start

### Local Development

1. Clone the repository:
```bash
git clone <repository-url>
cd pytonator
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

4. Run the application:
```bash
python -m pytonator
```

5. Access the API:
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Running Tests

```bash
# Run all tests
pytest

# Run unit tests only
pytest tests/unit/

# Run integration tests only
pytest tests/integration/

# Run with coverage
pytest --cov=pytonator --cov-report=html
```

### Code Quality

```bash
# Format code
black pytonator/ tests/

# Sort imports
isort pytonator/ tests/

# Lint code
flake8 pytonator/ tests/

# Type checking
mypy pytonator/
```

## API Endpoints

- `GET /` - Root endpoint
- `GET /health` - Health check
- `GET /api/v1/info` - Application information
- `GET /api/v1/status` - Application status
- `POST /api/v1/echo` - Echo message endpoint

## CI/CD Pipeline

The project includes a comprehensive GitLab CI/CD pipeline with the following stages:

1. **pytonator-build** - Build the application
2. **pytonator-test** - Run tests and code quality checks
3. **pytonator-security** - Security scanning with Trivy
4. **pytonator-container-build** - Build container image with Kaniko
5. **pytonator-deploy** - Deploy to staging and production

### Required GitLab Variables

Set these variables in your GitLab project settings:

- `REGISTRY_URL` - Container registry URL
- `REGISTRY_USER` - Registry username
- `REGISTRY_PASSWORD` - Registry password
- `LOCAL_ECR_URL` - Local ECR registry URL for pipeline images
- `LOCAL_ECR_USER` - Local ECR username
- `LOCAL_ECR_PASSWORD` - Local ECR password

## Development

### Project Structure

```
pytonator/
├── pytonator/           # Main application package
│   ├── __init__.py
│   ├── main.py         # FastAPI application
│   ├── config.py       # Configuration settings
│   └── routes.py       # API routes
├── tests/              # Test suite
│   ├── unit/           # Unit tests
│   └── integration/    # Integration tests
├── requirements.txt    # Production dependencies
├── requirements-dev.txt # Development dependencies
├── setup.py           # Package setup
├── Dockerfile         # Container configuration
├── .gitlab-ci.yml     # CI/CD pipeline
└── README.md          # This file
```

### Contributing

1. Create a feature branch: `git checkout -b feature/TICKET-123-description`
2. Make your changes
3. Run tests: `pytest`
4. Check code quality: `flake8`, `black`, `isort`, `mypy`
5. Commit your changes
6. Push and create a merge request

## License

MIT License - see LICENSE file for details.
```

This comprehensive CI/CD pipeline for the "pytonator" Python application includes:

### Key Features:

1. **Proper Stage Naming**: Uses `{application_name}-{stage_name}` format (e.g., `pytonator-build`, `pytonator-test`)

2. **Kaniko Integration**: Replaced Docker with Kaniko for secure container building

3. **Security Scanning**: Comprehensive Trivy scanning for file system, dependencies, and containers

4. **Python-Specific Configuration**: 
   - Proper Python version management
   - Comprehensive testing with pytest
   - Code quality tools (Black, isort, flake8, mypy)
   - Coverage reporting

5. **Branch Validation**: Enforces feature branch naming with ticket numbers

6. **Multi-Environment Deployment**: Staging and production deployment stages

7. **Complete Application**: Full FastAPI application with tests, documentation, and proper project structure

### Pipeline Stages:

1. **pytonator-build**: Compiles and packages the Python application
2. **pytonator-test**: Runs unit/integration tests and code quality checks
3. **pytonator-security**: Performs security scanning with Trivy
4. **pytonator-container-build**: Builds container image using Kaniko
5. **pytonator-deploy**: Deploys to staging and production environments

The pipeline follows all the project-specific rules and includes proper security measures, testing, and deployment practices.