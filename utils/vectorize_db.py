import argparse
import pandas as pd
import chromadb
from chromadb.api.models.Collection import Collection
from openai import OpenAI
from dotenv import load_dotenv
import os
import httpx

from config import RAGConfig

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_PROXY = os.getenv("OPENAI_PROXY")

if OPENAI_PROXY.lower() == "none":
	OPENAI_PROXY = None

config = RAGConfig()

def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("--csv-file", type=str, required=True, help="Path to CSV file")
	parser.add_argument("--db-path", type=str, default=config.db_path, help="Path to vector database")
	parser.add_argument("--collection", type=str, default=config.collection_name, help="Collection name")
	parser.add_argument("--batch-size", type=int, default=config.batch_size, help="Batch size")
	return parser.parse_args()


def read_data_from_csv(csv_file_path: str) -> pd.DataFrame:
	df = pd.read_csv(csv_file_path)
	return df


def prepare_text(df: pd.DataFrame):
	def format_row(row):
		return f"""
		Артикул: {row['id']}. Название: {row['name']}. Категория: {row['category']}. 
		Цена: {row['price']}. Описание: {row['description']}. Характеристики: {row['specs']}. 
		Бренд: {row['brand']}. Рейтинг: {row['rating']}. В наличии: {row['stock']}. 
		Вес: {row['weight']}. Цвет: {row['color']}. Гарантия: {row['warranty']}. 
		Год выпуска: {row['release_year']}. Скидка: {row['discount']}. Доступен: {row['is_available']}. 
		Память: {row['storage']}. Оперативная память: {row['ram']}. Размер экрана: {row['display_size']}. 
		Батарея: {row['battery']}. Лучше всего для: {row['best_for']}
		"""

	df["full_text"] = df.apply(
		lambda row: format_row(row),
		axis=1
	)


def init_chromadb(path: str, collection_name: str) -> Collection:
	client = chromadb.PersistentClient(path=path)
	collection = client.get_or_create_collection(name=collection_name)

	return collection


def create_chunks(text, chunk_size=config.chunk_size, chunk_overlap=config.chunk_overlap):
	chunks = []
	start = 0

	while start < len(text):
		end = start + chunk_size
		chunk = text[start:end]
		chunks.append(chunk)

		if end >= len(text):
			break
		start = end - chunk_overlap
	
	return chunks


def process_data(df: pd.DataFrame) -> tuple[list, list, list]:
	all_chunks = []
	all_metadatas = []
	all_ids = []

	for idx, row in df.iterrows():
		chunks = create_chunks(row["full_text"])

		for chunk_idx, chunk in enumerate(chunks):
			chunk_id = f"doc_{idx}_chunk_{chunk_idx}"

			all_chunks.append(chunk)
			all_metadatas.append({
				"source": row["name"],
				"row_index": idx,
				"chunk_index": chunk_idx
			})
			all_ids.append(chunk_id)

	return all_chunks, all_metadatas, all_ids


def get_embeddings(texts):
	openai_client = OpenAI(
		api_key=OPENAI_API_KEY,
		http_client=httpx.Client(
			proxy=OPENAI_PROXY,
			timeout=httpx.Timeout(30.0, connect=10.0)
		)
	)

	response = openai_client.embeddings.create(
		model=config.embedding_model,
		input=texts
	)
	return [data.embedding for data in response.data]


def process_batches(all_chunks: list, batch_size: int = config.batch_size) -> list:
	embeddings = []

	for i in range(0, len(all_chunks), batch_size):
		batch = all_chunks[i:i+batch_size]
		batch_embeddings = get_embeddings(batch)
		embeddings.extend(batch_embeddings)


	return embeddings


def add_into_vectorize_database(collection: Collection, embeddings: list, all_chunks: list, all_metadatas: list, all_ids: list):
	collection.add(
		embeddings=embeddings,
		documents=all_chunks,
		metadatas=all_metadatas,
		ids=all_ids
	)


def main():
	args = parse_arguments()

	data = read_data_from_csv(args.csv_file)
	prepare_text(data)
	collection = init_chromadb(path=args.db_path, collection_name=args.collection)
	all_chunks, all_metadatas, all_ids = process_data(data)
	embeddings = process_batches(all_chunks, batch_size=args.batch_size)
	
	add_into_vectorize_database(
		collection=collection,
		embeddings=embeddings,
		all_chunks=all_chunks,
		all_metadatas=all_metadatas,
		all_ids=all_ids
	)


if __name__ == "__main__":
	main()