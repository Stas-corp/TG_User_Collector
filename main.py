import asyncio
import logging

from app.bot import dp, bot
from app.config import settings
from app.database.engine import init_db


async def main() -> None:
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(levelname)s [%(asctime)s] %(name)s: %(message)s",
    )
    logger = logging.getLogger(__name__)
    
    await init_db()
    logger.info("Database initialized")
    
    logger.info("Starting bot with polling...")
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
