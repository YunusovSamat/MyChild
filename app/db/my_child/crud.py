import datetime
from typing import Optional
from uuid import UUID

from app.db.my_child.models import Child, Educator, Food, Event, Meal, Ration


async def get_educator_by_username(username: str) -> Optional[Educator]:
    return await Educator.get_or_none(username=username)


async def create_child(child: dict):
    return await Child.create(**child)


async def get_child(child_id: UUID):
    return await Child.get_or_none(child_id=child_id)


async def update_child(child_id: UUID, child: dict):
    await Child.filter(child_id=child_id).update(**child)


def get_all_child(educator_id: UUID):
    return Child.filter(educator_id=educator_id).all()


async def delete_child(child_id: UUID):
    delete_count = await Child.filter(child_id=child_id).delete()
    return delete_count


async def create_food(food: dict):
    return await Food.create(**food)


def get_all_foods(educator_id: UUID):
    return Food.filter(educator_id=educator_id).all()


async def get_food(food_id: UUID):
    return await Food.get_or_none(food_id=food_id)


async def delete_food(food_id: UUID):
    delete_count = await Food.filter(food_id=food_id).delete()
    return delete_count


async def create_event(event: dict):
    return await Event.create(**event)


async def create_meal(meal: dict):
    return await Meal.create(**meal)


async def create_ration(ration: dict):
    return await Ration.create(**ration)


async def get_event(child_id: UUID, date: datetime.date):
    return await Event.get_or_none(child_id=child_id, date=date)


async def delete_event(child_id: UUID, date: datetime.date):
    delete_count = await Event.filter(child_id=child_id, date=date).delete()
    return delete_count
