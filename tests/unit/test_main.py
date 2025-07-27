"""
Unit tests for main application module
"""

from pytonator.config import get_settings
from pytonator.main import app
from pytonator.routes import router


def test_app_import():
    """Test that the app can be imported"""
    assert app is not None
    assert app.title == "Pytonator"


def test_config_import():
    """Test that config can be imported and works"""
    settings = get_settings()
    assert settings is not None
    assert settings.app_name == "pytonator"
    assert settings.version == "0.1.0"


def test_routes_import():
    """Test that routes can be imported"""
    assert router is not None


def test_app_routes_registered():
    """Test that routes are registered in the app"""
    routes = [route.path for route in app.routes]
    assert "/health" in routes
    assert "/" in routes


def test_config_defaults():
    """Test configuration defaults"""
    settings = get_settings()
    assert settings.host == "0.0.0.0"
    assert settings.port == 8000
    assert settings.debug is False


def test_app_metadata():
    """Test application metadata"""
    assert app.description == "A Python application for CI/CD testing"
    assert app.version == "0.1.0"
