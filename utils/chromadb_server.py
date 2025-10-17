import chromadb
from chromadb.config import Settings

# Запуск: python chroma_server.py
client = chromadb.Client(Settings(
    chroma_server_host="localhost",
    chroma_server_http_port=8000,
    chroma_server_ssl_enabled=False,
    persist_directory="./chroma_db"
))


print("ChromaDB server running on http://localhost:8000")
input("Press Enter to stop...")