import os
from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Request, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.api.dependencies import auth
from app.api.dependencies.photo import get_photo_path
from app.db.my_child import crud
from app.db.my_child.models import Child, Educator, Parent
from app.schemas.models import ChildCreatePydantic

router = APIRouter()


@router.get("/children/")
async def read_children(
    current_educator: Educator = Depends(auth.get_current_educator),
):
    db_children = crud.get_all_child(current_educator.educator_id)
    if not db_children:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Children not found")
    ChildPydantic = pydantic_model_creator(Child, exclude=("events", "educator"))
    return await ChildPydantic.from_queryset(db_children)


@router.get("/children/{child_id}/")
async def read_child(
    child_id: UUID,
    current_user: Union[Educator, Parent] = Depends(auth.get_current_user),
):
    db_child = await crud.get_child(child_id)
    if not db_child:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Child {child_id} not found")
    ChildPydantic = pydantic_model_creator(Child, exclude=("events", "educator"))
    return await ChildPydantic.from_tortoise_orm(db_child)


@router.post(
    "/children/", status_code=status.HTTP_201_CREATED,
)
async def create_child(
    child: ChildCreatePydantic,
    request: Request,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    if not child.educator_id:
        child.educator_id = current_educator.educator_id
    placeholder_link = f"{request.base_url}photos/placeholder.jpg"
    child_dict = child.dict()
    child_dict["photo_link"] = placeholder_link

    db_child = await crud.create_child(child_dict)
    ChildPydantic = pydantic_model_creator(Child, exclude=("events", "educator"))
    return await ChildPydantic.from_tortoise_orm(db_child)


@router.put("/children/{child_id}/")
async def update_child(
    child_id: UUID,
    child: ChildCreatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    if not child.educator_id:
        child.educator_id = current_educator.educator_id
    await crud.update_child(child_id, child.dict(exclude_defaults=True))
    db_child = await crud.get_child(child_id)
    ChildPydantic = pydantic_model_creator(Child, exclude=("events", "educator"))
    return await ChildPydantic.from_tortoise_orm(db_child)


@router.delete("/children/{child_id}/")
async def delete_child(
    child_id: UUID, current_educator: Educator = Depends(auth.get_current_educator),
):
    delete_count = await crud.delete_child(child_id)
    if not delete_count:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Child {child_id} not found")
    photo_name = f"{child_id}.jpg"
    try:
        photo_path = await get_photo_path(photo_name)
    except HTTPException:
        pass
    else:
        os.remove(photo_path)

    return {"message": f"Deleted child {child_id}"}
