import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
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
    
    await message.answer('Ok')
