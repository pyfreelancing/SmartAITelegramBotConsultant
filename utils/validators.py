from aiogram.types import CallbackQuery, Message
import pandas as pd

from utils.config import RAGConfig

def is_valid_category_callback(callback: CallbackQuery) -> bool:
	categories = pd.read_csv(RAGConfig().csv_file)["category"].unique().tolist()
	return callback.data in categories


def is_valid_budget_callback(callback: CallbackQuery) -> bool:
	return (
		callback.data == "below_20k_rub" or \
		callback.data == "from_20k_to_60k_rub" or \
		callback.data == "from_60k_to_100k_rub" or \
		callback.data == "above_100k_rub" or \
		callback.data == "any_budget"
		)
