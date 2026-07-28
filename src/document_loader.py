from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path: str):
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Dosya bulunamadı: {file_path}")

    loader = PyPDFLoader(str(path))
    documents= loader.load()

    return documents