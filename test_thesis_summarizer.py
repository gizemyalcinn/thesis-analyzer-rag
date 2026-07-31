from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import ChatOllama

from thesis_section_extractor_legacy import extract_thesis_sections
from src.thesis_summarizer import summarize_thesis_sections


DOCS_FOLDER = Path("docs")


def get_first_pdf() -> Path:
    """Docs klasöründeki ilk PDF dosyasını bulur."""

    pdf_files = sorted(DOCS_FOLDER.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "docs klasöründe test edilecek PDF bulunamadı."
        )

    return pdf_files[0]


def create_llm() -> ChatOllama:
    """Tez özetlemesinde kullanılacak Ollama modelini oluşturur."""

    return ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        num_ctx=4096,
        num_predict=300,
        keep_alive="30m",
    )


def main() -> None:
    """PDF bölümlerini çıkarır ve ayrı ayrı özetler."""

    pdf_path = get_first_pdf()

    print(f"\nİncelenen tez: {pdf_path.name}\n")

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    print("Tez bölümleri çıkarılıyor...")

    sections = extract_thesis_sections(documents)

    print(f"{len(sections)} bölüm bulundu.\n")

    llm = create_llm()

    summaries = summarize_thesis_sections(
        llm=llm,
        sections=sections,
    )

    print("\n" + "=" * 70)
    print("TEZ BÖLÜM ÖZETLERİ")
    print("=" * 70)

    for section_name, summary in summaries.items():
        print(f"\n{section_name}\n")
        print(summary)
        print("\n" + "-" * 70)


if __name__ == "__main__":
    main()