from typing import Optional

from app.db.my_child.models import Educator


async def get_educator_by_username(username: str) -> Optional[Educator]:
    return await Educator.get_or_none(username=username)
