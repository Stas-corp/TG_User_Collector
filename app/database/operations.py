from datetime import datetime, UTC

from sqlalchemy import Select, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import Chat, User, UserChat


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


async def upsert_user_chat(session: AsyncSession, user_id: int, chat_id: int) -> UserChat:
    stmt: Select = select(UserChat).where(
        UserChat.user_id == user_id, UserChat.chat_id == chat_id
    )
    res = await session.execute(stmt)
    uc: UserChat = res.scalar_one_or_none()
    if uc:
        uc.last_seen_at = datetime.now(UTC)
    else:
        uc = UserChat(user_id=user_id, chat_id=chat_id)
        session.add(uc)
    await session.commit()
    await session.refresh(uc)
    return uc


async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    return await session.get(User, user_id)