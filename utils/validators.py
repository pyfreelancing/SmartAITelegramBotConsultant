from aiogram.types import CallbackQuery, Message


def is_valid_category_callback(callback: CallbackQuery) -> bool:
	return (
		callback.data == "laptops" or \
		callback.data == "smartphones"
		)


def is_valid_category_message(message: Message) -> bool:
	return (
		"ноутбук" in message.text.lower() or \
		"смартфон" in message.text.lower()
	)


def is_valid_budget_callback(callback: CallbackQuery) -> bool:
	return (
		callback.data == "below 20" or \
		callback.data == "from 20 to 60" or \
		callback.data == "from 60 to 100" or \
		callback.data == "above 100"
		)


def is_valid_budget_message(message: Message) -> bool:
	return (
		message.text.isdigit()
	)
