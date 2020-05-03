from uuid import UUID

from app.db.my_child.models import BotXBot, BotXChat, BotXCTS, BotXUser


async def get_user_by_huid(huid: UUID) -> BotXUser:
    return await BotXUser.get(user_huid=huid)


async def get_user_cts_by_huid(huid: UUID) -> BotXCTS:
    return await BotXCTS.get(users__user_huid=huid)


async def get_personal_chat_for_user(user_huid: UUID) -> BotXChat:
    return await BotXChat.get(
        members__user_huid=user_huid,
        cts__bots__current_bot=True,
        chat_type=ChatTypes.chat,
    )


async def get_current_bot_cts_by_host(host: str) -> BotXCTS:
    return await BotXCTS.get(host=host, bots__current_bot=True)


async def get_current_bot_by_host(host: str) -> BotXBot:
    return await BotXBot.get(cts_id=host, current_bot=True)
