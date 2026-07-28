from langchain_ollama import OllamaEmbeddings

def create_embedding_model():
    embeddings= OllamaEmbeddings(
        model= "embeddinggemma"
    )
    return embeddings