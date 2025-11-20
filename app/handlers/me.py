from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.operations import get_user_by_id

router = Router()


@router.message(Command("me"))
async def cmd_me(message: Message, session: AsyncSession, get_text: callable):
    user = await get_user_by_id(session, message.from_user.id)
    if not user:
        await message.answer(f"{get_text('no_information')}")
        return
    
    text = (
        f"<b>{get_text('profile_title')}</b>\n\n"
        f"{get_text('user_id')}: <code>{user.telegram_user_id}</code>\n"
        f"{get_text('username')}: "
        f"{('@' + user.username) if user.username else 'N/A'}\n"
        f"{get_text('first_name')}: {user.first_name or 'N/A'}\n"
        f"{get_text('last_name')}: {user.last_name or 'N/A'}\n"
        f"{get_text('language')}: {user.language_code or 'N/A'}\n"
        f"{get_text('registered')}: "
        f"{user.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{get_text('last_updated')}: "
        f"{user.updated_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
    )
    await message.answer(text)