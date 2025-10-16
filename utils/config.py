from dataclasses import dataclass



@dataclass
class RAGConfig:
		csv_file: str = "data/products.csv"
		db_path: str = "./chroma_db"
		collection_name: str = "products"
		openai_model: str = "gpt-4.1-nano"
		embedding_model: str = "text-embedding-3-small"
		batch_size: int = 100
		chunk_size: int = 500
		chunk_overlap: int = 50
		n_results: int = 3