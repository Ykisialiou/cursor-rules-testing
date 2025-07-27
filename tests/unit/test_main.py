"""
Unit tests for main application module
"""

from fastapi.testclient import TestClient
from pytonator.main import app

client = TestClient(app)


class TestMainApp:
    """Test main application functionality"""

    def test_app_creation(self):
        """Test that the app is created successfully"""
        assert app is not None
        assert hasattr(app, 'routes')


class TestHealthEndpoint:
    """Test health check endpoint"""

    def test_health_check(self):
        """Test health check endpoint returns 200"""
        response = client.get("/health")
        assert response.status_code == 200


class TestInfoEndpoint:
    """Test info endpoint"""

    def test_info_endpoint(self):
        """Test info endpoint returns 200"""
        response = client.get("/api/v1/info")
        assert response.status_code == 200


class TestStatusEndpoint:
    """Test status endpoint"""

    def test_status_endpoint(self):
        """Test status endpoint returns 200"""
        response = client.get("/api/v1/status")
        assert response.status_code == 200


class TestEchoEndpoint:
    """Test echo endpoint"""

    def test_echo_endpoint(self):
        """Test echo endpoint returns correct data"""
        test_data = {"message": "test"}
        response = client.post("/api/v1/echo", json=test_data)
        assert response.status_code == 200
        assert response.json() == test_data


class TestConfig:
    """Test configuration"""

    def test_config_loading(self):
        """Test that configuration loads properly"""
        from pytonator.config import get_settings
        settings = get_settings()
        assert settings is not None
