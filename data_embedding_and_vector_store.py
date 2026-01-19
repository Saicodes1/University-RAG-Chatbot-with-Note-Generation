from data_reading_and_splitting import total_files
from sentence_transformers import SentenceTransformer
import chromadb

texts=total_files()
for list_of_docs in texts:
  model = SentenceTransformer("nomic-ai/nomic-embed-text-v1", trust_remote_code=True)
  embeddings_data=model.encode([doc.page_content for doc in list_of_docs])

  client=chromadb.PersistentClient()
  collection=client.get_or_create_collection(name="Computer_Networks")
  metadatas = [
    {"Chapter_name": doc.metadata.get("Chapter_name", "Unknown")}
    for doc in list_of_docs
]

  collection.add(
      ids=[str(i) for i in range(len(list_of_docs))],
      documents=[doc.page_content for doc in list_of_docs],
      embeddings=embeddings_data,
      metadatas=metadatas
  )
