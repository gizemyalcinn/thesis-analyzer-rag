import shutil
from pathlib import Path

from langchain_chroma import Chroma


CHROMA_PATH = Path("data/chroma")


def create_vector_store(
    chunks,
    embeddings,
    reset: bool = True,
):
    """
    Creates a persistent Chroma vector store.

    If reset is True, the existing vector database is deleted
    before indexing the current documents.
    """

    if reset and CHROMA_PATH.exists():
        shutil.rmtree(CHROMA_PATH)

    CHROMA_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_PATH),
    )

    return vector_store


def load_vector_store(embeddings):
    """Loads the existing persistent Chroma vector store."""

    vector_store = Chroma(
        persist_directory=str(CHROMA_PATH),
        embedding_function=embeddings,
    )

    return vector_store