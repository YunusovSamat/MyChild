import base64
import os
import uuid

from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import FileResponse
from starlette import status

from app.api.dependencies.photo import get_photo_path
from app.db.my_child import crud
from app.schemas.models import PhotoCreatePydantic, PhotoDeletePydantic

router = APIRouter()


@router.get("/photos/{photo_name}")
async def read_photo(photo_path: str = Depends(get_photo_path)):
    return FileResponse(photo_path)


@router.post("/photos/")
async def upload_photo(photo_data: PhotoCreatePydantic, request: Request):
    photo_name = f"{uuid.uuid4()}.jpg"
    new_photo_link = f"{request.base_url}photos/{photo_name}"
    if photo_data.profile == "child":
        db_child = await crud.get_child(photo_data.id)
        if not db_child:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Child not found")
        old_photo_link = db_child.photo_link
        await crud.update_child(photo_data.id, {"photo_link": new_photo_link})
    else:
        db_parent = await crud.get_parent(photo_data.id)
        if not db_parent:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Parent not found")
        old_photo_link = db_parent.photo_link
        await crud.update_parent(photo_data.id, {"photo_link": new_photo_link})

    old_photo_name = os.path.split(old_photo_link)[1]
    if old_photo_name != "placeholder.jpg":
        old_photo_path = f"app/static/photos/{old_photo_name}"
        os.remove(old_photo_path)

    photo_bytes = base64.b64decode(photo_data.photo_base64)
    with open(f"app/static/photos/{photo_name}", "wb") as photo_file:
        photo_file.write(photo_bytes)
    return {"photo_link": new_photo_link}


@router.delete("/photos/")
async def delete_photo(photo_data: PhotoDeletePydantic, request: Request):
    placeholder_link = f"{request.base_url}photos/placeholder.jpg"

    if photo_data.profile == "child":
        db_child = await crud.get_child(photo_data.id)
        if not db_child:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Child not found")
        old_photo_link = db_child.photo_link
        await crud.update_child(photo_data.id, {"photo_link": placeholder_link})
    else:
        db_parent = await crud.get_parent(photo_data.id)
        if not db_parent:
            raise HTTPException(status.HTTP_404_NOT_FOUND, f"Parent not found")
        old_photo_link = db_parent.photo_link
        await crud.update_parent(photo_data.id, {"photo_link": placeholder_link})
    old_photo_name = os.path.split(old_photo_link)[1]
    if old_photo_name != "placeholder.jpg":
        old_photo_path = f"app/static/photos/{old_photo_name}"
        os.remove(old_photo_path)

    return {"photo_link": placeholder_link}
