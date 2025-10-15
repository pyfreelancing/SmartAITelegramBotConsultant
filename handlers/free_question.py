from aiogram import Router, types
from aiogram.fsm.context import FSMContext

from states.free_question import FreeQuestion

router = Router()


@router.callback_query(lambda callback: callback.data == "free_question")
async def start_free_question(callback: types.CallbackQuery, state: FSMContext):
	await callback.message.answer("Пожалуйста, задайте свой вопрос нашему консультату в свободной форме")
	await state.set_state(FreeQuestion.waiting_for_question)
	await callback.answer()