"""
API routes for pytonator
"""

from fastapi import APIRouter, HTTPException
from typing import Dict, Any

router = APIRouter()

@router.get("/info")
async def get_info() -> Dict[str, Any]:
    """Get application information"""
    return {
        "name": "pytonator",
        "version": "0.1.0",
        "status": "running",
        "description": "A Python application for CI/CD demonstration"
    }

@router.get("/status")
async def get_status() -> Dict[str, Any]:
    """Get application status"""
    return {
        "status": "operational",
        "uptime": "running",
        "checks": {
            "database": "connected",
            "cache": "available",
            "external_services": "healthy"
        }
    }

@router.post("/echo")
async def echo_message(message: Dict[str, str]) -> Dict[str, str]:
    """Echo back the provided message"""
    if "message" not in message:
        raise HTTPException(status_code=400, detail="Message field is required")
    return {"echo": message["message"]} 