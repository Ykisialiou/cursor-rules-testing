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