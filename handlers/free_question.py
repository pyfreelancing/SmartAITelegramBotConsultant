from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from keyboards.inline_keyboards import free_question_keyboard, finish_keyboard
from states.free_question import FreeQuestion
from utils import gpt

router = Router()


@router.callback_query(lambda callback: callback.data == "free_question")
async def start_free_question(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Пожалуйста, задайте свой вопрос нашему консультату в свободной форме")
	await state.set_state(FreeQuestion.waiting_for_question)
	await callback.answer()


@router.message(FreeQuestion.waiting_for_question)
async def process_free_question(message: types.Message, state: FSMContext):
	await message.answer("Обрабатываю ваш вопрос. Пожалуйста, подождите...")
	response = await gpt.get_response(message.text)
	end = "\n\nВас устроил ответ?"

	await message.answer(response+end, reply_markup=free_question_keyboard())

	await state.set_state(FreeQuestion.waiting_for_confirmation)


@router.callback_query(
	FreeQuestion.waiting_for_confirmation,
	lambda callback: callback.data == "free_question_yes"
	)
async def free_question_yes(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Благодарим за обращение. Хорошего дня!", reply_markup=finish_keyboard())
	await state.clear()
	await callback.answer()


@router.callback_query(
	FreeQuestion.waiting_for_confirmation,
	lambda callback: callback.data == "free_question_no"
)
async def free_question_no(callback: types.CallbackQuery, state: FSMContext):
	await start_free_question(callback, state)