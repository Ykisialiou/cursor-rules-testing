"""
Unit tests for the Flask application
"""

from pytonator import create_app


def test_app_creation():
    """Test that the Flask app can be created"""
    app = create_app()
    assert app is not None
    assert app.name == "pytonator"


def test_app_config():
    """Test app configuration"""
    app = create_app()
    assert app.config["DEBUG"] is False
    assert app.config["SECRET_KEY"] is not None


def test_blueprint_registration():
    """Test that blueprints are registered"""
    app = create_app()
    assert "main" in app.blueprints


def test_time_endpoint_exists():
    """Test that the time endpoint route exists"""
    app = create_app()
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    assert "/time" in routes
