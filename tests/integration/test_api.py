"""
Integration tests for the Flask application
"""

from datetime import datetime, timezone

from pytonator import create_app


def test_time_endpoint():
    """Test the /time endpoint returns current UTC time"""
    app = create_app()
    client = app.test_client()

    response = client.get("/time")
    assert response.status_code == 200

    data = response.get_json()
    assert "time" in data
    assert "timezone" in data
    assert data["timezone"] == "UTC"

    # Verify the time is recent (within last minute)
    response_time = datetime.fromisoformat(data["time"])
    current_time = datetime.now(timezone.utc)
    time_diff = abs((current_time - response_time).total_seconds())
    assert time_diff < 60  # Should be within 60 seconds


def test_time_endpoint_format():
    """Test the /time endpoint returns proper JSON format"""
    app = create_app()
    client = app.test_client()

    response = client.get("/time")
    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_time_endpoint_methods():
    """Test that only GET method is allowed on /time endpoint"""
    app = create_app()
    client = app.test_client()

    # POST should not be allowed
    response = client.post("/time")
    assert response.status_code == 405  # Method Not Allowed
