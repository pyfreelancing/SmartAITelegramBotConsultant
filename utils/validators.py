from aiogram.types import CallbackQuery, Message
import pandas as pd

from utils.config import RAGConfig

def is_valid_category_callback(callback: CallbackQuery) -> bool:
	categories = pd.read_csv(RAGConfig().csv_file)["category"].unique().tolist()
	return callback.data in categories


def is_valid_budget_callback(callback: CallbackQuery) -> bool:
	return (
		callback.data == "below 20" or \
		callback.data == "from 20 to 60" or \
		callback.data == "from 60 to 100" or \
		callback.data == "above 100"
		)
