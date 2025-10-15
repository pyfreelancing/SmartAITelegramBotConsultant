import asyncio
from aiogram import Bot, Dispatcher

from dotenv import load_dotenv
import os

from handlers import commands, free_question, search

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def main():
	bot = Bot(token=BOT_TOKEN)
	dp = Dispatcher()
	dp.include_router(commands.router)
	dp.include_router(free_question.router)
	dp.include_router(search.router)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())