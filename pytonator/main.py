"""
Main application module for pytonator
"""

from fastapi import FastAPI
from pytonator.config import get_settings
from pytonator.routes import router

# Create FastAPI application
app = FastAPI(
    title="Pytonator",
    description="A Python application for CI/CD testing",
    version="0.1.0"
)

# Include API routes
app.include_router(router, prefix="/api/v1")


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "pytonator"}


@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Pytonator!", "version": "0.1.0"}


if __name__ == "__main__":
    import uvicorn
    settings = get_settings()
    uvicorn.run(app, host=settings.host, port=settings.port)
