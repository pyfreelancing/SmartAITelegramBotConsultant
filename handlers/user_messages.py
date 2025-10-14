from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states.search_query import SearchQuery
from states.free_question import FreeQuestion
from keyboards.inline_keyboards import category_keyboard, budget_keyboard
from utils.validators import (
	is_valid_category_callback, is_valid_category_message,
	is_valid_budget_callback, is_valid_budget_message
)

router = Router()


@router.callback_query(lambda callback: callback.data == "search_query")
async def start_search(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Выберите категорию: ", reply_markup=category_keyboard())
	await state.set_state(SearchQuery.waiting_for_category)
	await callback.answer()


@router.callback_query(lambda callback: callback.data == "free_question")
async def start_free_question(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Пожалуйста, задайте свой вопрос нашему консультату в свободной форме")
	await state.set_state(FreeQuestion.waiting_for_question)
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


@router.message(SearchQuery.waiting_for_category)
async def process_category_manual(message: types.Message, state: FSMContext):
	if not is_valid_category_message(message):
		await message.answer("Пожалуйста, укажите правильную категорию")
		return
	
	await message.answer("Введите бюджет:", reply_markup=budget_keyboard())
	await state.update_data(category=message.text)
	await state.set_state(SearchQuery.waiting_for_budget)


@router.callback_query(
	SearchQuery.waiting_for_budget,
	lambda callback: is_valid_budget_callback(callback)
)
async def process_budget_by_button(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Ищу подходящий вариант...")
	await state.update_data(budget=callback.data)
	await state.set_state(SearchQuery.waiting_for_results)
	await callback.answer()


@router.message(SearchQuery.waiting_for_budget)
async def process_budget_manual(message: types.Message, state: FSMContext):
	if not is_valid_budget_message(message):
		await message.answer("Пожалуйста, введите бюджет цифрами")
		return
	
	await message.answer("Ищу подходящий вариант...")
	await state.update_data(budget=message.text)
	await state.set_state(SearchQuery.waiting_for_results)