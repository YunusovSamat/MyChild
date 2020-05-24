import base64
import datetime
import os
import uuid
from uuid import UUID

from fastapi import APIRouter, Depends, Request, HTTPException
from starlette import status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.api.dependencies import auth
from app.db.my_child import crud
from app.db.my_child.models import Educator, Gallery
from app.schemas.models import GalleryCreatePydantic, GalleryPydantic

router = APIRouter()


@router.get("/gallery/")
async def read_gallery(
    current_educator: Educator = Depends(auth.get_current_educator)
):
    db_gallery = crud.get_gallery_by_educator_id(current_educator.educator_id)
    return await GalleryPydantic.from_queryset(db_gallery)


@router.post("/gallery/")
async def create_gallery(
    gallery: GalleryCreatePydantic,
    request: Request,
    current_educator: Educator = Depends(auth.get_current_educator)
):
    photo_name = f'{uuid.uuid4()}.jpg'
    photo_link = f"{request.base_url}gallery/{photo_name}"
    photo_bytes = base64.b64decode(gallery.photo_base64)
    with open(f'app/static/gallery/{photo_name}', 'wb') as photo_file:
        photo_file.write(photo_bytes)

    gallery_dict = gallery.dict()
    gallery_dict["educator_id"] = current_educator.educator_id
    gallery_dict["photo_link"] = photo_link
    gallery_dict["timestamp"] = datetime.datetime.utcnow()

    db_gallery = await crud.create_gallery(gallery_dict)
    return await GalleryPydantic.from_tortoise_orm(db_gallery)


@router.delete("/gallery/gallery_id/")
async def delete_gallery(
    gallery_id: UUID,
    current_educator: Educator = Depends(auth.get_current_educator)
):
    db_gallery = await crud.get_gallery(gallery_id)
    if not db_gallery:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Gallery not found")
    photo_name = os.path.split(db_gallery.photo_link)[1]
    photo_path = f'app/static/gallery/{photo_name}'
    if os.path.exists(photo_path):
        os.remove(photo_path)

    await crud.delete_gallery(gallery_id)

    return await GalleryPydantic.from_tortoise_orm(db_gallery)
