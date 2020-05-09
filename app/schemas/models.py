import datetime
from typing import List

from pydantic import UUID4
from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.db.my_child.models import Educator
from app.db.my_child.models import Food
from app.db.my_child.models import Parent

EducatorPydantic = pydantic_model_creator(
    Educator, name="Educator", exclude=("password",)
)
EducatorCreatePydantic = pydantic_model_creator(
    Educator, name="EducatorCreate", exclude=("educator_id",)
)


class ChildCreatePydantic(BaseModel):
    age: int = None
    photo_link: str = None
    blood_type: str = None
    group: str = None
    locker_num: str = None
    name: str = None
    surname: str = None
    patronymic: str = None
    educator_id: UUID4 = None


class FoodCreatePydantic(BaseModel):
    name: str = None
    educator_id: UUID4 = None


FoodPydantic = pydantic_model_creator(Food, exclude=("educator_id",))


class RationCreatePydantic(BaseModel):
    food_id: UUID4 = None
    denial: bool = None


class MealCreatePydantic(BaseModel):
    type: int = None
    rations: List[RationCreatePydantic] = None


class EventCreatePydantic(BaseModel):
    child_id: UUID4 = None
    date: datetime.date = None
    has_come: str = None
    has_gone: str = None
    asleep: str = None
    awoke: str = None
    comment: str = None
    meals: List[MealCreatePydantic] = None


ParentPydantic = pydantic_model_creator(Parent, exclude=("password",))


class ParentBasePydantic(BaseModel):
    child_id: UUID4 = None
    relation_degree: str = None
    phone: str = None
    photo_link: str = None
    name: str = None
    surname: str = None
    patronymic: str = None


class ParentCreatePydantic(ParentBasePydantic):
    username: str
    password: str
    second_password: str


class ParentUpdatePydantic(ParentBasePydantic):
    password: str = None
    second_password: str = None


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None
