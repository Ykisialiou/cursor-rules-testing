"""
Integration tests for API endpoints
"""

from fastapi.testclient import TestClient

from pytonator.main import app

client = TestClient(app)


def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data
    assert data["message"] == "Welcome to Pytonator!"


def test_health_endpoint():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["service"] == "pytonator"


def test_info_endpoint():
    """Test info endpoint"""
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "pytonator"
    assert data["version"] == "0.1.0"


def test_status_endpoint():
    """Test status endpoint"""
    response = client.get("/api/v1/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "operational"


def test_echo_endpoint():
    """Test echo endpoint"""
    test_message = "Hello, World!"
    response = client.post("/api/v1/echo", json={"message": test_message})
    assert response.status_code == 200
    data = response.json()
    assert data["echo"] == test_message


def test_echo_endpoint_invalid_request():
    """Test echo endpoint with invalid request"""
    response = client.post("/api/v1/echo", json={"invalid_field": "test"})
    assert response.status_code == 422  # Validation error
