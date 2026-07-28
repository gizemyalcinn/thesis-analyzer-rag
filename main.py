from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.embedding_model import create_embedding_model
from src.vector_store import create_vector_store


documents = load_pdf("docs/sample.pdf")
chunks = split_documents(documents)

embedding_model = create_embedding_model()

vector_store = create_vector_store(
    chunks,
    embedding_model
)

print("Vector database oluşturuldu.")