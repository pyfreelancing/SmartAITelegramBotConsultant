import asyncio

from init import bot, dp
from handlers import commands, free_question, search, finish


async def main():
	dp.include_router(commands.router)
	dp.include_router(free_question.router)
	dp.include_router(search.router)
	dp.include_router(finish.router)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())