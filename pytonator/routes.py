"""
Routes for the Flask application
"""

from datetime import datetime, timezone

from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)


@bp.route("/time")
def get_time():
    """Get current UTC time"""
    current_time = datetime.now(timezone.utc)
    return jsonify({"time": current_time.isoformat(), "timezone": "UTC"})
