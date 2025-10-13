import asyncio
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
import os

from handlers import user_commands, user_messages

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
	bot = Bot(token=BOT_TOKEN)
	dp = Dispatcher()
	dp.include_router(user_commands.router)
	dp.include_router(user_messages.router)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())