import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.operations import upsert_chat, upsert_user, upsert_user_chat

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message, session: AsyncSession):
    user_data = {
        "telegram_user_id": message.from_user.id,
        "username": message.from_user.username,
        "first_name": message.from_user.first_name,
        "last_name": message.from_user.last_name,
        "language_code": message.from_user.language_code,
        "is_bot": message.from_user.is_bot,
    }
    chat_data = {
        "chat_id": message.chat.id,
        "type": message.chat.type,
        "title": getattr(message.chat, "title", None),
    }
    logging.info(f"Data\nUser_data:{user_data}\nChat_data:{chat_data}")
    
    user = await upsert_user(session, user_data)
    chat = await upsert_chat(session, chat_data)
    await upsert_user_chat(session, user.telegram_user_id, chat.chat_id)
    logging.info("DB write OK")
    
    await message.answer('Ok')
