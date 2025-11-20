from typing import Any, Awaitable, Callable, Dict
from functools import partial

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, User

from app.utils.localization import get_text


class LocalizationMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        user: User | None = data.get("event_from_user")
        
        lang = "en"
        if user and user.language_code:
            if user.language_code.startswith("uk"):
                lang = "uk"
        
        data["get_text"] = partial(get_text, lang=lang)
        
        return await handler(event, data)