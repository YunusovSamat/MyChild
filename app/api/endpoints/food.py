from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import auth
from app.db.my_child import crud
from app.db.my_child.models import Educator
from app.schemas.models import FoodCreatePydantic, FoodPydantic

router = APIRouter()


@router.post("/foods/")
async def create_food(
    food: FoodCreatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    if not food.educator_id:
        food.educator_id = current_educator.educator_id
    db_food = await crud.create_food(food.dict())
    return await FoodPydantic.from_tortoise_orm(db_food)


@router.get("/foods/")
async def read_foods(current_educator: Educator = Depends(auth.get_current_educator)):
    db_foods = crud.get_all_foods(current_educator.educator_id)
    return await FoodPydantic.from_queryset(db_foods)


@router.get("/foods/{food_id}/")
async def read_food(
    food_id: UUID, current_educator: Educator = Depends(auth.get_current_educator)
):
    db_food = await crud.get_food(food_id)
    return await FoodPydantic.from_tortoise_orm(db_food)


@router.delete("/foods/{food_id}/")
async def delete_food(
    food_id: UUID, current_educator: Educator = Depends(auth.get_current_educator)
):
    delete_count = await crud.delete_food(food_id)
    if not delete_count:
        raise HTTPException(status.HTTP_404_NOT_FOUND, f"Food {food_id} not found")
    return {"message": f"Deleted food {food_id}"}
