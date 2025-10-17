from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


def start_keyboard():
	keyboard = InlineKeyboardBuilder()
	query_button = InlineKeyboardButton(text="Найти подходящее устройство по фильтрам", callback_data="search_query")
	free_question_button = InlineKeyboardButton(text="Задать вопрос свободно", callback_data="free_question")
	keyboard.add(query_button, free_question_button)
	keyboard.adjust(1)
	return keyboard.as_markup()


def category_keyboard():
	keyboard = InlineKeyboardBuilder()
	laptops_button = InlineKeyboardButton(text="Ноутбуки", callback_data="laptop")
	smartphones_button = InlineKeyboardButton(text="Смартфоны", callback_data="smartphone")
	tablet_button = InlineKeyboardButton(text="Планшеты", callback_data="tablet")
	wearable_button = InlineKeyboardButton(text="Смартчасы", callback_data="wearable")
	audio_button = InlineKeyboardButton(text="Наушники", callback_data="audio")
	camera_button = InlineKeyboardButton(text="Камеры", callback_data="camera")
	keyboard_button = InlineKeyboardButton(text="Клавиатуры", callback_data="keyboard")
	mouse_button = InlineKeyboardButton(text="Мышки", callback_data="mouse")
	smart_home_button = InlineKeyboardButton(text="Умные колонки", callback_data="smart_home")
	gaming_console_button = InlineKeyboardButton(text="Игровые консоли", callback_data="gaming_console")
	gaming_handheld_button = InlineKeyboardButton(text="Портативные игровые консоли", callback_data="gaming_handheld")

	keyboard.add(
		laptops_button, smartphones_button, tablet_button,
		wearable_button, audio_button, camera_button,
		keyboard_button, mouse_button, smart_home_button,
		gaming_console_button, gaming_handheld_button)
	keyboard.adjust(1)
	return keyboard.as_markup()


def budget_keyboard():
	keyboard = InlineKeyboardBuilder()
	below_20_button = InlineKeyboardButton(text="До 20.000 рублей", callback_data="below_20k_rub")
	from_20_to_60_button = InlineKeyboardButton(text="От 20.000 до 60.000 рублей", callback_data="from_20k_to_60k_rub")
	from_60_to_100_button = InlineKeyboardButton(text="От 60.000 до 100.000 рублей", callback_data="from_60k_to_100k_rub")
	above_100_button = InlineKeyboardButton(text="Свыше 100.000 рублей", callback_data="above_100k_rub")
	any_budget_button = InlineKeyboardButton(text="Любой бюджет", callback_data="any_budget")
	keyboard.add(below_20_button, from_20_to_60_button, from_60_to_100_button, above_100_button, any_budget_button)
	keyboard.adjust(1)
	return keyboard.as_markup()


def free_question_keyboard():
	keyboard = InlineKeyboardBuilder()
	yes_button = InlineKeyboardButton(text="Да, спасибо", callback_data="free_question_yes")
	no_button = InlineKeyboardButton(text="Нет, задать другой", callback_data="free_question_no")
	keyboard.add(yes_button, no_button)
	keyboard.adjust(1)
	return keyboard.as_markup()


def finish_keyboard():
	keyboard = InlineKeyboardBuilder()
	return_button = InlineKeyboardButton(text="Вернуться в главное меню", callback_data="return_main_menu")
	keyboard.add(return_button)
	return keyboard.as_markup()