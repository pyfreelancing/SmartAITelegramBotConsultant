from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states.search_query import SearchQuery
from keyboards.inline_keyboards import category_keyboard, budget_keyboard, finish_keyboard
from utils.validators import (
	is_valid_category_callback,	is_valid_budget_callback
)
from utils import gpt

router = Router()


@router.callback_query(lambda callback: callback.data == "search_query")
async def start_search(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Выберите категорию: ", reply_markup=category_keyboard())
	await state.set_state(SearchQuery.waiting_for_category)
	await callback.answer()


@router.callback_query(
	SearchQuery.waiting_for_category, 
	lambda callback: is_valid_category_callback(callback)
	)
async def process_category_by_button(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Введите бюджет:", reply_markup=budget_keyboard())
	await state.update_data(category=callback.data)
	await state.set_state(SearchQuery.waiting_for_budget)
	await callback.answer()


@router.callback_query(
	SearchQuery.waiting_for_budget,
	lambda callback: is_valid_budget_callback(callback)
)
async def process_budget_by_button(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Ищу подходящий вариант...")
	await state.update_data(budget=callback.data)
	await state.set_state(SearchQuery.waiting_for_results)

	data = await state.get_data()
	query = f"Категория: {data["category"]}. Цена: {data["budget"]}"
	
	response = await gpt.get_response(query)

	await callback.message.answer(response, reply_markup=finish_keyboard())
	await callback.answer()
