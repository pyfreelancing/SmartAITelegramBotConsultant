from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.search_query import SearchQuery
from keyboards.inline_keyboards import start_keyboard, category_keyboard
from other.templates import get_start_message_template

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
	start_message = get_start_message_template()
	await message.answer(start_message, reply_markup=start_keyboard())