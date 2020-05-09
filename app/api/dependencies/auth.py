from datetime import datetime
from datetime import timedelta
from typing import Union

import jwt
from fastapi import Depends
from fastapi import HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

from app.core.config import ALGORITHM
from app.core.config import SECRET_KEY
from app.db.my_child import crud
from app.db.my_child.models import Educator, Parent
from app.schemas.models import TokenData
from app.services.security import oauth2_scheme
from app.services.security import verify_password

SECRET_KEY = str(SECRET_KEY)


async def authenticate_user(username: str, password: str) -> Union[Educator, Parent, bool]:
    db_user = await crud.get_user_by_username(username)
    if not db_user:
        return False
    if not verify_password(password, db_user.password):
        return False
    return db_user


def create_access_token(*, data: dict, expires_delta: timedelta) -> bytes:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)) -> Union[Educator, Parent]:
    credentials_exception = HTTPException(
        status_code=HTTP_401_UNAUTHORIZED, detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except jwt.PyJWTError:
        raise credentials_exception
    db_user = await crud.get_user_by_username(token_data.username)
    if db_user is None:
        raise credentials_exception
    return db_user


async def get_current_educator(user: Union[Educator, Parent] = Depends(get_current_user)) -> Educator:
    if not isinstance(user, Educator):
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Prohibited. you do not have rights"
        )
    return user


async def get_current_parent(user: Union[Educator, Parent] = Depends(get_current_user)) -> Parent:
    if not isinstance(user, Parent):
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Prohibited. you do not have rights"
        )
    return user
