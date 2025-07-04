import asyncio
import logging

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from astr0puzzle_handlers import router
bot = Bot(token="7802187208:AAHophu7BlRC2yaJyuAw3QpdKsDKAWXxNo0")
dp = Dispatcher()




async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")