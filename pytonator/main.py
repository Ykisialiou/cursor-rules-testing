"""
Main entry point for the pytonator application
"""

import uvicorn
from fastapi import FastAPI
from pytonator.config import settings
from pytonator.routes import router

app = FastAPI(
    title="Pytonator",
    description="A Python application for CI/CD demonstration",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    """Root endpoint"""
    return {"message": "Welcome to Pytonator!", "version": "0.1.0"}

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "pytonator"}

def main():
    """Main function to run the application"""
    uvicorn.run(
        "pytonator.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )

if __name__ == "__main__":
    main() 