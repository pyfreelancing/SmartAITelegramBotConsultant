import chromadb
import os
import httpx
from openai import AsyncOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from dotenv import load_dotenv

from utils.config import RAGConfig
from other.templates import get_gpt_request_template

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_PROXY = os.getenv("OPENAI_PROXY")



class RAGManager:
	def __init__(self, config: RAGConfig):
		self.config = config
		self._chromadb_client = None
		self._chromadb_collection = None
		self._openai_client = None
		self._llm = None


	async def initialize(self):
		# Initialize OpenAI client
		self._openai_client = AsyncOpenAI(
			api_key=OPENAI_API_KEY,
			http_client=httpx.AsyncClient(
				proxy=OPENAI_PROXY,
				timeout=httpx.Timeout(30.0, connect=10.0)
			)
		)

		# Initialize LLM
		self._llm = ChatOpenAI(
			api_key=OPENAI_API_KEY,
			model=self.config.openai_model,
			openai_proxy=OPENAI_PROXY,
			temperature=0.1
		)

		# Initialize Chromadb client
		self._chromadb_client = await chromadb.AsyncHttpClient(
			host="localhost",
			port=8000,
			ssl=False
		)

		await self._chromadb_client.heartbeat()
		self._chromadb_collection = await self._chromadb_client.get_collection(self.config.collection_name)


	async def _search_similar_documents(self, query: str, n_results: int):
		embedding_response = await self._openai_client.embeddings.create(
			model=self.config.embedding_model,
			input=[query]
		)
		
		query_embedding = embedding_response.data[0].embedding

		results = await self._chromadb_collection.query(
			query_embeddings=[query_embedding],
			n_results=n_results
		)

		return results


	def _get_prompt_template(self):
		template = get_gpt_request_template()
		prompt = ChatPromptTemplate.from_template(template)
		return prompt


	async def get_response(self, user_question: str) -> str:
		search_results = await self._search_similar_documents(
			query=user_question,
			n_results=self.config.n_results
		)
		documents = search_results["documents"][0]
		metadatas = search_results["metadatas"][0]

		context_text = "\n\n".join([
			f"Источник: {meta["source"]}\nТекст: {doc}"
			for doc, meta in zip(documents, metadatas)
		])

		prompt = self._get_prompt_template()
		final_prompt = prompt.format(context=context_text, question=user_question)
		response = self._llm.invoke(final_prompt)

		return response.content