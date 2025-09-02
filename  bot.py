import asyncio
import os
from aiogram import Bot, Dispatcher
from handlers import start
from dotenv import load_dotenv

load_dotenv()

TOKEN = str(os.getenv("TOKEN_BOT"))
# if TOKEN is None:
#     raise ValueError("TOKEN не задан в переменных окружения")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(start.cmd_start())

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())