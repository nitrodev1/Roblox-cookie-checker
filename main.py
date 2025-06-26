import asyncio
import sys
import sqlite3
from aiogram import Bot, Dispatcher
from app.handlers import router
from config import TOKEN
from time import time as __

bot = Bot(token=TOKEN)
dp = Dispatcher()




async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print('бот включен. все логи будут отображаться в этой консоли.')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Отключаю бота...')
