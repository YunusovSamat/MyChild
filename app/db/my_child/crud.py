from typing import Optional
from uuid import UUID

from app.db.my_child.models import Child, Educator, Parent
from app.schemas.models import ChildCreatePydantic


async def get_educator_by_username(username: str) -> Optional[Educator]:
    return await Educator.get_or_none(username=username)


async def create_child(child: ChildCreatePydantic):
    return await Child.create(**child.dict())


async def get_child(child_id: UUID):
    return await Child.get_or_none(child_id=child_id)


async def update_child(child_id: UUID, child: ChildCreatePydantic):
    await Child.filter(child_id=child_id).update(**child.dict())


def get_all_child(educator_id: UUID):
    return Child.filter(educator_id=educator_id).all()


async def delete_child(child_id: UUID):
    delete_count = await Child.filter(child_id=child_id).delete()
    return delete_count


def get_parents_by_child_id(child_id: UUID):
    return Parent.filter(child_id=child_id).all()
