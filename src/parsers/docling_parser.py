import re
from pathlib import Path

from docling.document_converter import DocumentConverter


def parse_markdown_sections(markdown_text: str) -> list[dict]:
    """
    Docling Markdown çıktısındaki ## başlıklarını
    ve bu başlıkların altındaki metinleri ayırır.
    """

    sections = []

    pattern = re.compile(
        r"^##\s+(.+?)\s*$",
        flags=re.MULTILINE,
    )

    matches = list(pattern.finditer(markdown_text))

    for index, match in enumerate(matches):
        title = match.group(1).strip()

        content_start = match.end()

        if index + 1 < len(matches):
            content_end = matches[index + 1].start()
        else:
            content_end = len(markdown_text)

        content = markdown_text[
            content_start:content_end
        ].strip()

        sections.append(
            {
                "title": title,
                "content": content,
            }
        )

    return sections


def parse_pdf(pdf_path: str | Path) -> list[dict]:
    """
    PDF'yi Docling ile dönüştürür ve bölümlere ayırır.
    """

    converter = DocumentConverter()
    result = converter.convert(str(pdf_path))

    markdown_text = result.document.export_to_markdown()

    return parse_markdown_sections(markdown_text)