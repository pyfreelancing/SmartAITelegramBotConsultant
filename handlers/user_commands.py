from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states.search_query import SearchQuery
from keyboards.inline_keyboards import start_keyboard, category_keyboard

router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
	await message.answer("Привет!", reply_markup=start_keyboard())


@router.message(Command("search"))
async def cmd_search(message: types.Message, state: FSMContext):
	await message.answer("Выберите категорию: ", reply_markup=category_keyboard())
	await state.set_state(SearchQuery.waiting_for_category)