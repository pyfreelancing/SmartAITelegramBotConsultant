from aiogram import Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
import asyncio

from states.search_query import SearchQuery
from keyboards.inline_keyboards import category_keyboard

router = Router()

@router.callback_query(
	SearchQuery.waiting_for_category, 
	lambda callback: callback.data == "laptops" or \
		callback.data == "smartphones"
	)
async def process_category_by_button(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Введите бюджет:")
	await state.update_data(category=callback.data)
	await callback.answer()


@router.message(SearchQuery.waiting_for_category)
async def process_category_manual(message: types.Message, state: FSMContext):
	if not ("ноутбук" in message.text.lower() or "смартфон" in message.text.lower()):
		await message.answer("Пожалуйста, укажите правильную категорию")
		return
	
	await message.answer("Введите бюджет:")
	await state.update_data(category=message.text)
	await state.set_state(SearchQuery.waiting_for_budget)