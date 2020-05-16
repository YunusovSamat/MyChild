import os

from fastapi import HTTPException
from starlette import status


async def get_photo_path(photo_name: str) -> str:
    if os.path.dirname(photo_name):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Path contains folder")
    file_extension = os.path.splitext(photo_name)[1]
    if file_extension != ".jpg":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "File is not .jpg")
    photo_path = f"app/statics/photos/{photo_name}"
    if not os.path.isfile(photo_path):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Photo is not exist")
    return photo_path
