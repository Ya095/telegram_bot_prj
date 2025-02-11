import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from config import settings
from routers import router as main_router


async def main():
    dp = Dispatcher()
    dp.include_router(main_router)

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    logging.basicConfig(level=logging.INFO)
    # проверка на новые события (в бесконечном цикле)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
