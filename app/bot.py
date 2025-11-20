from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from app.handlers import start, me
from app.config import settings
from app.middleware.database import DatabaseMiddleware
from app.middleware.L10n import LocalizationMiddleware


bot = Bot(
    token=settings.BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(me.router)

dp.update.middleware(DatabaseMiddleware())
dp.update.middleware(LocalizationMiddleware())