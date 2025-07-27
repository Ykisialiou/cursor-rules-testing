"""
Pytonator - A simple Flask application
"""

from flask import Flask

from pytonator.config import Config


def create_app():
    """Create and configure the Flask application"""
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import and register routes
    from pytonator.routes import bp

    app.register_blueprint(bp)

    return app
