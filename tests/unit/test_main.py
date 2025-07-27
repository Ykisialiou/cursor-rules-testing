"""
Unit tests for main application
"""

import pytest
from fastapi.testclient import TestClient
from pytonator.main import app

client = TestClient(app)

def test_root_endpoint():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to Pytonator!"
    assert data["version"] == "0.1.0"

def test_health_check():
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
    test_message = {"message": "Hello, Pytonator!"}
    response = client.post("/api/v1/echo", json=test_message)
    assert response.status_code == 200
    data = response.json()
    assert data["echo"] == "Hello, Pytonator!"

def test_echo_endpoint_missing_message():
    """Test echo endpoint with missing message"""
    response = client.post("/api/v1/echo", json={})
    assert response.status_code == 400 