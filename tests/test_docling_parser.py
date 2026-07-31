from pathlib import Path

from docling.document_converter import DocumentConverter


DOCS_FOLDER = Path("docs")


def get_first_pdf() -> Path:
    """docs klasöründeki ilk PDF dosyasını bulur."""

    pdf_files = sorted(DOCS_FOLDER.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "docs klasöründe test edilecek PDF bulunamadı."
        )

    return pdf_files[0]


def main() -> None:
    """PDF'yi Docling ile dönüştürür ve Markdown çıktısını kaydeder."""

    pdf_path = get_first_pdf()

    print(f"\nDönüştürülen PDF: {pdf_path.name}")
    print("Docling belgeyi analiz ediyor...\n")

    converter = DocumentConverter()
    result = converter.convert(pdf_path)

    markdown_text = result.document.export_to_markdown()

    output_path = Path("data/docling_output.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        markdown_text,
        encoding="utf-8",
    )

    print("Dönüştürme tamamlandı.")
    print(f"Çıktı kaydedildi: {output_path}")
    print("\nİlk 2000 karakter:\n")
    print(markdown_text[:2000])


if __name__ == "__main__":
    main()