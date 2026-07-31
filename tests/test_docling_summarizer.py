from pathlib import Path

from langchain_ollama import ChatOllama

from src.parsers.docling_parser import parse_pdf
from src.section_mapper import map_sections
from src.thesis_summarizer import summarize_thesis_sections


PDF_PATH = Path("docs/tez.pdf")


def create_llm() -> ChatOllama:
    return ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        num_ctx=4096,
        num_predict=250,
        keep_alive="30m",
    )


def main() -> None:
    print("\nPDF Docling ile ayrıştırılıyor...")

    parsed_sections = parse_pdf(PDF_PATH)

    mapped_sections, unmapped_sections = map_sections(
        parsed_sections
    )

    print(
        f"{len(mapped_sections)} ana bölüm eşlendi."
    )

    if unmapped_sections:
        print(
            f"{len(unmapped_sections)} başlık eşlenemedi."
        )

    llm = create_llm()

    summaries = summarize_thesis_sections(
        llm=llm,
        sections=mapped_sections,
    )

    print("\n" + "=" * 70)
    print("BÖLÜM ÖZETLERİ")
    print("=" * 70)

    for section_name, summary in summaries.items():
        print(f"\n{section_name}\n")
        print(summary)
        print("\n" + "-" * 70)


if __name__ == "__main__":
    main()