from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def category_keyboard():
	keyboard = InlineKeyboardBuilder()
	laptops_button = InlineKeyboardButton(text="Ноутбуки", callback_data="laptops")
	smartphones_button = InlineKeyboardButton(text="Смартфоны", callback_data="smartphones")
	keyboard.add(laptops_button, smartphones_button)
	return keyboard.as_markup()


def budget_keyboard():
	keyboard = InlineKeyboardBuilder()
	below_20_button = InlineKeyboardButton(text="До 20.000 рулей", callback_data="below 20")
	from_20_to_60 = InlineKeyboardButton(text="От 20.000 до 60.000 рублей", callback_data="from 20 to 60")
	from_60_to_100 = InlineKeyboardButton(text="От 60.000 до 100.000 рублей", callback_data="from 60 to 100")
	above_100 = InlineKeyboardButton(text="Свыше 100.000 рублей", callback_data="above 100")
	keyboard.add(below_20_button, from_20_to_60, from_60_to_100, above_100)
	return keyboard.as_markup()