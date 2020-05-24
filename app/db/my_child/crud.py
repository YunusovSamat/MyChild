import datetime
from typing import List, Optional, Union
from uuid import UUID

from app.db.my_child.models import (
    Bill,
    Child,
    Educator,
    Event,
    Food,
    Meal,
    Parent,
    Ration, Gallery,
)


async def get_user_by_username(username: str) -> Optional[Union[Educator, Parent]]:
    user = await Educator.get_or_none(username=username)
    if not user:
        user = await Parent.get_or_none(username=username)
    return user


async def get_educator_by_username(username: str) -> Optional[Educator]:
    return await Educator.get_or_none(username=username)


async def get_parent_by_username(username: str) -> Optional[Parent]:
    return await Parent.get_or_none(username=username)


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


async def get_parent(parent_id: UUID):
    return await Parent.get_or_none(parent_id=parent_id)


async def create_parent(parent: dict):
    return await Parent.create(**parent)


async def update_parent(parent_id: UUID, parent: dict):
    await Parent.filter(parent_id=parent_id).update(**parent)


async def get_bill(bill_id: UUID):
    return await Bill.get_or_none(bill_id=bill_id)


def get_bill_by_child_id(child_id: UUID):
    return Bill.filter(child_id=child_id).all()


def get_bill_by_children_ids(children_ids: List[UUID]):
    return Bill.filter(child_id__in=children_ids).all()


async def create_bill(bill: dict):
    return await Bill.create(**bill)


async def update_bill(bill_id: UUID, bill: dict):
    return await Bill.filter(bill_id=bill_id).update(**bill)


async def delete_bill(bill_id: UUID):
    delete_count = await Bill.filter(bill_id=bill_id).delete()
    return delete_count


def get_gallery_by_educator_id(educator_id: UUID):
    return Gallery.filter(educator_id=educator_id).order_by("timestamp").all()


async def create_gallery(gallery: dict):
    return await Gallery.create(**gallery)


async def get_gallery(gallery_id: UUID):
    return await Gallery.get_or_none(gallery_id=gallery_id)


async def delete_gallery(gallery_id: UUID):
    delete_count = await Gallery.filter(gallery_id=gallery_id).delete()
    return delete_count
