from aiogram.fsm.state import State, StatesGroup



class SearchQuery(StatesGroup):
	waiting_for_category = State()
	waiting_for_budget = State()
	waiting_for_results = State()

