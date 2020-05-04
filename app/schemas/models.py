from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.db.my_child.models import Educator

EducatorPydantic = pydantic_model_creator(Educator, name="Educator", exclude=("password",))
EducatorCreatePydantic = pydantic_model_creator(
    Educator, name="EducatorCreate", exclude=("educator_id",))


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None
