from datetime import datetime, UTC

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Chat, User


async def upsert_user(session: AsyncSession, data: dict) -> User:
    user = await session.get(User, data["telegram_user_id"])
    if user:
        for k, v in data.items():
            if k != "telegram_user_id":
                setattr(user, k, v)
        user.updated_at = datetime.now(UTC)
    else:
        user = User(**data)
        session.add(user)
    await session.commit()
    await session.refresh(user)
    return user


async def upsert_chat(session: AsyncSession, data: dict) -> Chat:
    chat = await session.get(Chat, data["chat_id"])
    if chat:
        for k, v in data.items():
            if k != "chat_id":
                setattr(chat, k, v)
        chat.updated_at = datetime.now(UTC)
    else:
        chat = Chat(**data)
        session.add(chat)
    await session.commit()
    await session.refresh(chat)
    return chat