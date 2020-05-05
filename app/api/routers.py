from fastapi import APIRouter

from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.child import router as children_router
from app.api.endpoints.food import router as food_router
from app.api.endpoints.event import router as event_router

router = APIRouter()

router.include_router(auth_router, tags=["auth"])
router.include_router(children_router, tags=["children"])
router.include_router(food_router, tags=["foods"])
router.include_router(event_router, tags=["event"])
