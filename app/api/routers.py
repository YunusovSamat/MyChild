from fastapi import APIRouter

from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.bill import router as bill_router
from app.api.endpoints.child import router as children_router
from app.api.endpoints.event import router as events_router
from app.api.endpoints.food import router as foods_router
from app.api.endpoints.parent import router as parents_router
from app.api.endpoints.photo import router as photos_router
from app.api.endpoints.gallery import router as gallery_router

router = APIRouter()

router.include_router(auth_router, tags=["auth"])
router.include_router(children_router, tags=["children"])
router.include_router(foods_router, tags=["foods"])
router.include_router(events_router, tags=["events"])
router.include_router(parents_router, tags=["parents"])
router.include_router(photos_router, tags=["photos"])
router.include_router(bill_router, tags=["bill"])
router.include_router(gallery_router, tags=["gallery"])
