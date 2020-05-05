from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import auth
from app.db.my_child import crud
from app.db.my_child.models import Educator
from app.schemas.models import ChildCreatePydantic, ChildPydantic, ParentPydantic

router = APIRouter()


@router.get("/children/")
async def read_children(
    current_educator: Educator = Depends(auth.get_current_educator),
):
    db_children = crud.get_all_child(current_educator.educator_id)
    return await ChildPydantic.from_queryset(db_children)


@router.get("/children/{child_id}/")
async def read_child(
    child_id: UUID, current_educator: Educator = Depends(auth.get_current_educator)
):
    db_child = await crud.get_child(child_id)
    db_parents = crud.get_parents_by_child_id(child_id)

    result = (await ChildPydantic.from_tortoise_orm(db_child)).dict()
    result["parents"] = await ParentPydantic.from_queryset(db_parents)
    return result


@router.post(
    "/children/",
    status_code=status.HTTP_201_CREATED,
    response_model=ChildPydantic,
    description="Если educator_id null, то воспитатель будет текущим",
)
async def create_child(
    child: ChildCreatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    if not child.educator_id:
        child.educator_id = current_educator.educator_id
    db_child = await crud.create_child(child)
    return await ChildPydantic.from_tortoise_orm(db_child)


@router.put("/children/{child_id}/")
async def update_child(
    child_id: UUID,
    child: ChildCreatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    if not child.educator_id:
        child.educator_id = current_educator.educator_id
    await crud.update_child(child_id, child)
    db_child = await crud.get_child(child_id)
    return ChildPydantic.from_tortoise_orm(db_child)


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
