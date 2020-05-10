from datetime import datetime, timedelta
from typing import Union

import jwt
from fastapi import Depends, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN

from app.core.config import ALGORITHM, SECRET_KEY
from app.db.my_child import crud
from app.db.my_child.models import Educator, Parent
from app.schemas.models import TokenData
from app.services.security import oauth2_scheme, verify_password

SECRET_KEY = str(SECRET_KEY)


# async def authenticate_user(
#     username: str, password: str
# ) -> Union[Educator, Parent, bool]:
#     db_user = await crud.get_user_by_username(username)
#     if not db_user:
#         return False
#     if not verify_password(password, db_user.password):
#         return False
#     return db_user


async def authenticate_educator(
    username: str, password: str
) -> Union[Educator, bool]:
    db_educator = await crud.get_educator_by_username(username)
    if not db_educator:
        return False
    if not verify_password(password, db_educator.password):
        return False
    return db_educator


async def authenticate_parent(
    username: str, password: str
) -> Union[Parent, bool]:
    db_parent = await crud.get_parent_by_username(username)
    if not db_parent:
        return False
    if not verify_password(password, db_parent.password):
        return False
    return db_parent


def create_access_token(*, data: dict, expires_delta: timedelta) -> bytes:
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
    token: str = Depends(oauth2_scheme),
) -> Union[Educator, Parent]:
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


async def get_current_educator(
    user: Union[Educator, Parent] = Depends(get_current_user)
) -> Educator:
    if not isinstance(user, Educator):
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Prohibited. you do not have rights"
        )
    return user


async def get_current_parent(
    user: Union[Educator, Parent] = Depends(get_current_user)
) -> Parent:
    if not isinstance(user, Parent):
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Prohibited. you do not have rights"
        )
    return user
