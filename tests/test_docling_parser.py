from pathlib import Path

from docling.document_converter import DocumentConverter


DOCS_FOLDER = Path("docs")


def get_first_pdf() -> Path:
    

    pdf_files = sorted(DOCS_FOLDER.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError(
            "No PDF files found in the docs folder."
        )

    return pdf_files[0]


def main() -> None:

    pdf_path = get_first_pdf()

    print(f"\nProcessing PDF: {pdf_path.name}")
    print("Parsing document structure using Docling...\n")

    converter = DocumentConverter()
    result = converter.convert(pdf_path)

    markdown_text = result.document.export_to_markdown()

    output_path = Path("data/docling_output.md")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        markdown_text,
        encoding="utf-8",
    )

    print("Document parsing completed successfully.")
    print(f"Markdown file saved to: {output_path}")


if __name__ == "__main__":
    main()