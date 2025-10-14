from aiogram.fsm.state import State, StatesGroup



class FreeQuestion(StatesGroup):
	waiting_for_question = State()