from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.handlers import start
from app.config import settings
from app.middleware.database import DatabaseMiddleware


bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()

dp.include_router(start.router)

dp.update.middleware(DatabaseMiddleware())