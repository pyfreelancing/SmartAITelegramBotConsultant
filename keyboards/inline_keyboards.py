from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton



def category_keyboard():
	keyboard = InlineKeyboardBuilder()
	laptops_button = InlineKeyboardButton(text="Ноутбуки", callback_data="laptops")
	smartphones_button = InlineKeyboardButton(text="Смартфоны", callback_data="smartphones")
	keyboard.add(laptops_button, smartphones_button)
	return keyboard.as_markup()