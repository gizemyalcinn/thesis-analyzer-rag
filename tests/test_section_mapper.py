from pathlib import Path

from src.parsers.docling_parser import parse_pdf
from src.section_mapper import map_sections


PDF_PATH = Path("docs/tez.pdf")


def main() -> None:
    parsed_sections = parse_pdf(PDF_PATH)

    mapped_sections, unmapped_sections = map_sections(
        parsed_sections
    )

    print("\nEşlenen bölümler:\n")

    for section_name, content in mapped_sections.items():
        print(section_name)
        print(f"Kelime sayısı: {len(content.split())}")
        print(f"Başlangıç: {content[:150]}...")
        print("-" * 70)

    print("\nEşlenemeyen başlıklar:\n")

    for section in unmapped_sections:
        print(
            f"- {section['title']} "
            f"(seviye {section['heading_level']})"
        )


if __name__ == "__main__":
    main()