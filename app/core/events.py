from typing import Any, Callable

from app.db.events import close_db, init_db


def startup(**kwargs: Any) -> Callable:
    async def start_app() -> None:
        await init_db(**kwargs)

    return start_app


def shutdown() -> Callable:
    async def stop_app() -> None:
        await close_db()
    return stop_app
