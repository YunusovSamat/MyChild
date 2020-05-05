from fastapi import APIRouter

from app.api.endpoints.auth import router as auth_router
from app.api.endpoints.children import router as children_router

router = APIRouter()

router.include_router(auth_router, tags=["auth"])
router.include_router(children_router, tags=["children"])
