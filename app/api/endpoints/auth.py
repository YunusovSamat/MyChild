from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.dependencies import auth
from app.core.config import ACCESS_TOKEN_EXPIRE_MINUTES
from app.schemas.models import Token, UserRoleEnum

router = APIRouter()


@router.post("/token/{user_role}/", response_model=Token)
async def login_for_access_token(user_role: UserRoleEnum, form_data: OAuth2PasswordRequestForm = Depends()):
    if user_role == "educator":
        user = await auth.authenticate_educator(form_data.username, form_data.password)
    else:
        user = await auth.authenticate_parent(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
