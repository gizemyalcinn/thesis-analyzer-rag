from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader

from src.thesis_section_extractor import extract_thesis_sections


DOCS_FOLDER = Path("docs")


def get_first_pdf() -> Path:
    """Docs klasöründeki ilk PDF dosyasını bulur."""

    pdf_files = list(DOCS_FOLDER.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "docs klasöründe test edilecek PDF bulunamadı."
        )

    return pdf_files[0]


def main() -> None:
    """Tez bölümlerini çıkarır ve kısa bir kontrol çıktısı gösterir."""

    pdf_path = get_first_pdf()

    print(f"\nİncelenen tez: {pdf_path.name}")

    loader = PyPDFLoader(str(pdf_path))
    documents = loader.load()

    sections = extract_thesis_sections(documents)

    print("\nBulunan bölümler:\n")

    if not sections:
        print("Hiçbir bölüm bulunamadı.")
        return

    for section_name, section_text in sections.items():
        word_count = len(section_text.split())

        preview = (
            section_text[:150]
            .replace("\n", " ")
            .strip()
        )

        print(section_name)
        print(f"Kelime sayısı: {word_count}")
        print(f"Başlangıç: {preview}...")
        print("-" * 70)


if __name__ == "__main__":
    main()