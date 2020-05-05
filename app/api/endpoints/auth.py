from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies import auth
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.db.my_child import crud
from app.db.my_child.models import Educator
from app.schemas.models import EducatorPydantic, Token

router = APIRouter()


@router.post("/token/educator/", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    educator = await auth.authenticate_user(form_data.username, form_data.password)
    if not educator:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": educator.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/educator/")
async def get_educator():
    db_educator = await crud.get_educator_by_username("Irina")
    return await EducatorPydantic.from_tortoise_orm(db_educator)


@router.get("/educator/me/")
async def read_users_me(
    current_educator: Educator = Depends(auth.get_current_educator),
):
    return current_educator
