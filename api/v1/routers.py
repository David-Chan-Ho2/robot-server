from fastapi import APIRouter

from api.v1.endpoints import robots, health, webrtc

router = APIRouter()

router.include_router(health.router, prefix="/", tags=["Health"])

api_router = APIRouter(prefix='/api/v1')
api_router.include_router(robots.router, prefix="/robots", tags=["Robots"])
api_router.include_router(webrtc.router, prefix="/webrtc", tags=["webrtc"])

router.include_router(api_router)