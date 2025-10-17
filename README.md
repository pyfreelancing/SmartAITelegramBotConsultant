# SmartAITelegramBotConsultant

**О проекте**: Умный бот-констультант для интернет-магазина электронной техники, использующий **RAG** для ответов на основе базы товаров в формате `csv`.

**Стек технологий**: **aiogram**, **LangChain**, **RAG**, **OpenAI API**, **ChromaDB** 

**Возможности бота**:
- Диалог с подбором товара через FSM
- Свободные вопросы к AI-консультанту
- Рекомендации на основе базы товаров (RAG)

**Скриншоты и демо**:
- Запрос по фильтрам: 

![Запрос по фильтрам](filters.gif)

- Свободный запрос:

![Свободный запрос](free.gif)
- Ссылка на бота: [t.me/SmartAIDevicesConsultant_bot](https://t.me/SmartAIDevicesConsultant_bot)

**Установка и запуск**:
- `pip install -r requirements.txt`
- Настройка `.env`

**Структура проекта**:
- `data/` - папка с `.csv` файлами, содержащими данные о товарах:
	- `products.csv` - пример товаров
- `handlers/` - хэндлеры Telegram бота:
	- `commands.py` - хэндлер для команд через слэш "/"
	- `finish.py` - хэндлер для кнопки возврата к главному меню
	- `free_question.py` - хэндлер для работы с вопросами, заданными в свободной форме
	- `search.py` - хэндлер для подбора товара по фильтрам
- `keyboards/` - разметки кнопок в Telegram боте:
	- `inline_keyboards.py` - inline-кнопки
- `states/` - **FSM**:
	- `free_question.py` - **FSM** для работы со свободными вопросами
	- `search_query.py` - **FSM** для работы с поиском по фильтрам
- `utils/` - утилиты
	- `config.py` - конфиги (в частности конфиг для RAGManager'а)
	- `gpt.py` - функция запроса к AI
	- `rag_manager.py` - **RAG**-менеджер (организует весь процесс RAG)
	- `templates.py` - template'ы для **OpenAI** и ответов Telegram бота
	- `validators.py` - валидаторы для хэндлеров Telegram бота
	- `vectorize_db.py` - скрипт для создания/обновления **ChromaDB**
- `.env` - переменные виртуального окружения
- `init.py` - инициализация **bot**, **Dispatcher** и **RAGManager**
- `main.py` - запуск бота