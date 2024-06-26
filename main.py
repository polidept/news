from config import TOKEN
import asyncio
from aiogram import Bot, Dispatcher
from handlers.commands import router
import logging
import sys


async def main():
    bot = Bot(token = TOKEN)
    dp = Dispatcher()
    dp.include_router(router = router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO, stream = sys.stdout)
    try:
        asyncio.run(main())
    except Exception as e:
        print("Error", e)