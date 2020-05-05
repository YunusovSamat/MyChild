from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import auth
from app.db.my_child import crud
from app.db.my_child.models import Educator, Child
from app.schemas.models import ChildCreatePydantic
from tortoise.contrib.pydantic import pydantic_model_creator


router = APIRouter()


@router.get("/children/")
async def read_children(
    current_educator: Educator = Depends(auth.get_current_educator),
):
    db_children = crud.get_all_child(current_educator.educator_id)
    ChildPydantic = pydantic_model_creator(Child, exclude=("events", "educator"))
    return await ChildPydantic.from_queryset(db_children)


@router.get("/children/{child_id}/")
async def read_child(
    child_id: UUID,
    current_educator: Educator = Depends(auth.get_current_educator)
):
    db_child = await crud.get_child(child_id)
    ChildPydantic = pydantic_model_creator(Child, exclude=("events", "educator"))
    return await ChildPydantic.from_tortoise_orm(db_child)


@router.post(
    "/children/",
    status_code=status.HTTP_201_CREATED,
    description="Если educator_id null, то воспитатель будет текущим",
)
async def create_child(
    child: ChildCreatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    if not child.educator_id:
        child.educator_id = current_educator.educator_id
    db_child = await crud.create_child(child.dict())
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


@router.delete("/children/{child_id}")
async def delete_child(
    child_id: UUID, current_educator: Educator = Depends(auth.get_current_educator),
):
    delete_count = await crud.delete_child(child_id)
    if not delete_count:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Child {child_id} not found"
        )
    return {"message": f"Deleted child {child_id}"}
