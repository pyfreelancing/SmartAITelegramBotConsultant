from aiogram import Router, types

from keyboards.inline_keyboards import start_keyboard
from other.templates import get_start_message_template

router = Router()


@router.callback_query(lambda callback: callback.data == "return_main_menu")
async def return_to_main_menu(callback: types.CallbackQuery):
	start_message = get_start_message_template()
	await callback.message.answer(start_message, reply_markup=start_keyboard())
	await callback.answer()