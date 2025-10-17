from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from dotenv import load_dotenv
import os

from states.search_query import SearchQuery
from keyboards.inline_keyboards import start_keyboard
from other.templates import get_start_message_template
from init import ragman

load_dotenv()

ADMIN_ID = os.getenv("ADMIN_ID")

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
	start_message = get_start_message_template()
	await message.answer(start_message, reply_markup=start_keyboard())


@router.message(Command("update_db"))
async def cmd_update_db(message: types.Message):
	if message.from_user.id != int(ADMIN_ID):
		return 
	
	await message.answer("Начинаю обновление БД")
	await ragman.initialize()
	args = {
		"csv_file": "data/products.csv",
		"db_path": None,
		"collection": None,
		"batch_size": None
	}
	response = await ragman.update_db(args=args)
	await message.answer(response)