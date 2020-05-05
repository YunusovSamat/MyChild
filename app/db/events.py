from databases import DatabaseURL
from tortoise import Tortoise


async def init_db(dsn: DatabaseURL) -> None:
    await Tortoise.init(
        db_url=str(dsn), modules={"my_child": ["app.db.my_child.models"]}
    )


async def close_db() -> None:
    await Tortoise.close_connections()
