from init import ragman

async def get_response(message: str) -> str:
	await ragman.initialize()
	response = await ragman.get_response(user_question=message)
	return response