from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()


# @router.post("/photos/")
# async def create_upload_file(file: UploadFile = File(...)):
#     contents = await file.read()
#     return {"file": contents}


@router.get("/photos/")
async def read_photo():
    return FileResponse("app/statics/photo/placeholder.jpg")


# @router.get("/photos/{child_id}/")
# async def read_photo(photo: bytes)
