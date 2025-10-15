from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states.search_query import SearchQuery
from states.free_question import FreeQuestion
from keyboards.inline_keyboards import category_keyboard, budget_keyboard

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

