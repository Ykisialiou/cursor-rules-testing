"""
API routes for pytonator application
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class EchoRequest(BaseModel):
    """Echo request model"""

    message: str


class EchoResponse(BaseModel):
    """Echo response model"""

    echo: str


@router.get("/info")
async def get_info():
    """Get application information"""
    return {"name": "pytonator", "version": "0.1.0"}


@router.get("/status")
async def get_status():
    """Get application status"""
    return {"status": "operational"}


@router.post("/echo", response_model=EchoResponse)
async def echo_message(request: EchoRequest):
    """Echo back the provided message"""
    return EchoResponse(echo=request.message)
