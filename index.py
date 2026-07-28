from pathlib import Path

from src.document_loader import load_pdf
from src.text_splitter import split_documents
from src.embedding_model import create_embedding_model
from src.vector_store import create_vector_store


docs_path = Path("docs")
pdf_files = list(docs_path.glob("*.pdf"))

if not pdf_files:
    raise FileNotFoundError("docs klasöründe PDF bulunamadı.")

all_documents = []

for pdf_file in pdf_files:
    print(f"Okunuyor: {pdf_file.name}")

    documents = load_pdf(str(pdf_file))
    all_documents.extend(documents)

chunks = split_documents(all_documents)
embedding_model = create_embedding_model()

create_vector_store(
    chunks,
    embedding_model
)

print(f"\n{len(pdf_files)} PDF indekslendi.")
print(f"{len(chunks)} chunk oluşturuldu.")