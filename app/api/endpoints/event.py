import datetime
from typing import Union
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from tortoise.contrib.pydantic import pydantic_model_creator

from app.api.dependencies import auth
from app.db.my_child import crud
from app.db.my_child.models import Educator, Event, Parent
from app.schemas.models import EventCreatePydantic

router = APIRouter()


@router.post("/events/")
async def create_event(
    event: EventCreatePydantic,
    current_educator: Educator = Depends(auth.get_current_educator),
):
    await crud.delete_event(event.child_id, event.date)

    db_event = await crud.create_event(event.dict(exclude={"meals"}))
    for meal in event.meals:
        meal_dict = meal.dict(exclude={"rations"})
        meal_dict["event_id"] = db_event.event_id
        db_meal = await crud.create_meal(meal_dict)
        for ration in meal.rations:
            ration_dict = ration.dict(exclude={"food_name"})
            ration_dict["meal_id"] = db_meal.meal_id
            await crud.create_ration(ration_dict)
    return {"status": "created"}


@router.get("/events/")
async def read_event(
    child_id: UUID = Query(...),
    date: datetime.date = Query(...),
    current_user: Union[Educator, Parent] = Depends(auth.get_current_user),
):
    db_event = await crud.get_event(child_id, date)
    if not db_event:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Event not found")
    EventPydantic = pydantic_model_creator(Event, exclude=("child",))
    event = await EventPydantic.from_tortoise_orm(db_event)
    event_dict = event.dict()
    for meal_dict in event_dict["meals"]:
        meal_dict["rations"] = meal_dict["meal_rations"]
        del meal_dict["meal_rations"]
        for ration_dict in meal_dict["rations"]:
            food_dict = ration_dict["food"]
            for k, v in food_dict.items():
                ration_dict[k] = v
            del ration_dict["food"]
    return event_dict
