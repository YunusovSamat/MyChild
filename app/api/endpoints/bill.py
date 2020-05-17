from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.api.dependencies import auth
from app.db.my_child import crud
from app.db.my_child.models import Bill, Educator, Parent
from app.schemas.models import BillCreatePydantic, BillUpdatePydantic

router = APIRouter()


@router.get("/bill/{bill_id}/")
async def read_bill(
    bill_id: UUID,
    current_user: Union[Educator, Parent] = Depends(auth.get_current_user),
):
    db_bill = await crud.get_bill(bill_id)
    if not db_bill:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "bill not found")
    BillPydantic = pydantic_model_creator(
        Bill, exclude=("child.educator", "child.events", "child.parents")
    )
    return await BillPydantic.from_tortoise_orm(db_bill)


@router.get("/bill/")
async def read_all_bill(
    current_user: Union[Educator, Parent] = Depends(auth.get_current_user)
):
    if isinstance(current_user, Parent):
        db_bill = crud.get_bill_by_child_id(current_user.child_id)
    else:
        children_ids = [child.child_id for child in await current_user.children]
        db_bill = crud.get_bill_by_children_ids(children_ids)
    BillPydantic = pydantic_model_creator(
        Bill, exclude=("child.educator", "child.events", "child.parents")
    )
    return await BillPydantic.from_queryset(db_bill)


@router.post("/bill/")
async def create_bill(
    bill: BillCreatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    BillPydantic = pydantic_model_creator(
        Bill, exclude=("child.educator", "child.events", "child.parents")
    )
    if bill.child_id:
        db_bill = await crud.create_bill(bill.dict())
        return await BillPydantic.from_tortoise_orm(db_bill)
    else:
        children_ids = [child.child_id for child in await current_educator.children]
        for child_id in children_ids:
            bill_dict = bill.dict()
            bill_dict["child_id"] = child_id
            await crud.create_bill(bill_dict)
        db_bill = crud.get_bill_by_children_ids(children_ids)
        return await BillPydantic.from_queryset(db_bill)


@router.put("/bill/{bill_id}/")
async def update_bill(
    bill_id: UUID,
    bill: BillUpdatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    await crud.update_bill(bill_id, bill.dict(exclude_defaults=True))
    db_bill = await crud.get_bill(bill_id)
    BillPydantic = pydantic_model_creator(
        Bill, exclude=("child.educator", "child.events", "child.parents")
    )
    return await BillPydantic.from_tortoise_orm(db_bill)


@router.delete("/bill/{bill_id}/")
async def update_bill(
    bill_id: UUID, current_educator: Educator = Depends(auth.get_current_educator),
):
    delete_count = await crud.delete_bill(bill_id)
    if not delete_count:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "bill not found")
    return {"message": f"Deleted bill {bill_id}"}
