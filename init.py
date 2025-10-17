from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from utils.rag_manager import RAGManager
from utils.config import RAGConfig

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
ragman = RAGManager(config=RAGConfig())