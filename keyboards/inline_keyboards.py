from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def start_keyboard():
	keyboard = InlineKeyboardBuilder()
	query_button = InlineKeyboardButton(text="Найти подходящее устройство", callback_data="search_query")
	free_question_button = InlineKeyboardButton(text="Задать вопрос свободно", callback_data="free_question")
	keyboard.add(query_button, free_question_button)
	keyboard.adjust(1, 1)
	return keyboard.as_markup()


def category_keyboard():
	keyboard = InlineKeyboardBuilder()
	laptops_button = InlineKeyboardButton(text="Ноутбуки", callback_data="laptops")
	smartphones_button = InlineKeyboardButton(text="Смартфоны", callback_data="smartphones")
	keyboard.add(laptops_button, smartphones_button)
	keyboard.adjust(1, 1)
	return keyboard.as_markup()


def budget_keyboard():
	keyboard = InlineKeyboardBuilder()
	below_20_button = InlineKeyboardButton(text="До 20.000 рулей", callback_data="below 20")
	from_20_to_60_button = InlineKeyboardButton(text="От 20.000 до 60.000 рублей", callback_data="from 20 to 60")
	from_60_to_100_button = InlineKeyboardButton(text="От 60.000 до 100.000 рублей", callback_data="from 60 to 100")
	above_100_button = InlineKeyboardButton(text="Свыше 100.000 рублей", callback_data="above 100")
	keyboard.add(below_20_button, from_20_to_60_button, from_60_to_100_button, above_100_button)
	keyboard.adjust(1, 1, 1, 1)
	return keyboard.as_markup()


def free_question_keyboard():
	keyboard = InlineKeyboardBuilder()
	yes_button = InlineKeyboardButton(text="Да, спасибо", callback_data="free_question_yes")
	no_button = InlineKeyboardButton(text="Нет, задать другой", callback_data="free_question_no")
	keyboard.add(yes_button, no_button)
	keyboard.adjust(1, 1)
	return keyboard.as_markup()