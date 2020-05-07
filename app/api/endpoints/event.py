import datetime
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status, Query

from app.api.dependencies import auth
from app.db.my_child import crud
from app.db.my_child.models import Educator, Child, Event
from app.schemas.models import EventCreatePydantic
from tortoise.contrib.pydantic import pydantic_model_creator
import pydantic

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
async def read_event(child_id: UUID = Query(...), date: datetime.date = Query(...)):
    db_event = await crud.get_event(child_id, date)
    if not db_event:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, detail=f"Event not found"
        )
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
# {
#     "event_id": "11935c9d-8f12-4437-9488-ca1b97188114",
#     "date": "2020-05-05",
#     "has_come": "string",
#     "has_gone": "string",
#     "asleep": "string",
#     "awoke": "string",
#     "comment": "string",
#     "child_id": "540a1403-5962-47a0-8197-02afc878786a",
#     "meals": [
#         {
#             "meal_id": "a2e6eeb3-f731-4c09-a4a1-0641d8d1ae89",
#             "type": 1,
#             "meal_rations": [
#                 {
#                     "ration_id": "748f3a48-de02-49c6-8497-124c0902cfb6",
#                     "food": {
#                         "food_id": "3305b7dc-3328-4b19-8105-ce42756762a2",
#                         "name": "\u041a\u0430\u0448\u0430"
#                     },
#                     "denial": true
#                 }
#             ]
#         }
#     ]
# }
