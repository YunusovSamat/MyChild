from pydantic import UUID4
from pydantic.main import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from app.db.my_child.models import Child, Educator, Parent

EducatorPydantic = pydantic_model_creator(
    Educator, name="Educator", exclude=("password",)
)
EducatorCreatePydantic = pydantic_model_creator(
    Educator, name="EducatorCreate", exclude=("educator_id",)
)

ChildPydanticBase = pydantic_model_creator(Child, name="Child")
ChildCreatePydanticBase = pydantic_model_creator(
    Child, name="ChildCreate", exclude=("child_id",)
)


class ChildPydantic(ChildPydanticBase):
    educator_id: UUID4


class ChildCreatePydantic(ChildCreatePydanticBase):
    educator_id: UUID4 = None


ParentPydantic = pydantic_model_creator(Parent, exclude=("password",))


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None
