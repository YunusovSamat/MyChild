from typing import Any, Callable

from asyncpg.pgproto import pgproto
from pydantic.json import ENCODERS_BY_TYPE

from app.db.events import close_db, init_db


def startup(**kwargs: Any) -> Callable:
    ENCODERS_BY_TYPE[pgproto.UUID] = str

    async def start_app() -> None:
        await init_db(**kwargs)

    return start_app


def shutdown() -> Callable:
    async def stop_app() -> None:
        await close_db()

    return stop_app
