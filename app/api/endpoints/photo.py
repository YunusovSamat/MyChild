import base64
import os

from fastapi import APIRouter, HTTPException, status, Depends, Request
from fastapi.responses import FileResponse
from pydantic import UUID4
from starlette.routing import NoMatchFound

from app.api.dependencies.photo import get_photo_path
from app.db.my_child import crud
from app.schemas.models import PhotoCreatePydantic, PhotoDeletePydantic

router = APIRouter()


@router.get("/photos/{photo_name}")
async def read_photo(photo_path: str = Depends(get_photo_path)):
    return FileResponse(photo_path)


@router.post("/photos/")
async def upload_photo(photo_data: PhotoCreatePydantic, request: Request):
    photo_link = f"{request.base_url}photos/{photo_data.id}.jpg"
    if photo_data.profile == "child":
        await crud.update_child(photo_data.id, {"photo_link": photo_link})
    else:
        await crud.update_parent(photo_data.id, {"photo_link": photo_link})

    photo_bytes = base64.b64decode(photo_data.photo_base64)
    with open(f"app/statics/photos/{photo_data.id}.jpg", 'wb') as photo_file:
        photo_file.write(photo_bytes)
    return {"photo_link": photo_link}


@router.delete("/photos/")
async def delete_photo(photo_data: PhotoDeletePydantic, request: Request):
    photo_name = f"{photo_data.id}.jpg"
    photo_path = await get_photo_path(photo_name)
    os.remove(photo_path)
    placeholder_link = f"{request.base_url}photos/placeholder.jpg"

    if photo_data.profile == "child":
        await crud.update_child(photo_data.id, {"photo_link": placeholder_link})
    else:
        await crud.update_parent(photo_data.id, {"photo_link": placeholder_link})
    return {"photo_link": placeholder_link}
