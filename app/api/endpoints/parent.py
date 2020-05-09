from datetime import timedelta
from uuid import UUID

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.api.dependencies import auth
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.db.my_child import crud
from app.db.my_child.models import Child, Parent
from app.db.my_child.models import Educator
from app.schemas.models import ParentPydantic, ParentCreatePydantic, ParentUpdatePydantic
from app.services.security import get_password_hash

router = APIRouter()


@router.post("/parents/")
async def create_parent(parent: ParentCreatePydantic):
    db_parent = await crud.get_parent_by_username(parent.username)
    if db_parent:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username is already exist"
        )
    if parent.password != parent.second_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="first and second passwords do not match"
        )
    parent.password = get_password_hash(parent.password)
    db_parent = await crud.create_parent(parent.dict(exclude={"second_password"}))
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": db_parent.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.put("/parents/")
async def update_parent(parent: ParentUpdatePydantic, current_parent: Parent = Depends(auth.get_current_parent)):
    if parent.password != parent.second_password:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="first and second passwords do not match"
        )
    if parent.password:
        parent.password = get_password_hash(parent.password)
    await crud.update_parent(current_parent.parent_id, parent.dict(exclude_defaults=True, exclude={"second_password"}))
    db_parent = await crud.get_parent_by_username(current_parent.username)
    return await ParentPydantic.from_tortoise_orm(db_parent)


@router.get("/parents/me/")
async def read_current_parent(
    current_parent: Parent = Depends(auth.get_current_parent),
):
    db_parent = await crud.get_parent_by_username(current_parent.username)
    return await ParentPydantic.from_tortoise_orm(db_parent)
