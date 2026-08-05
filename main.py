from pathlib import Path

from langchain_ollama import ChatOllama

from src.embedding_model import create_embedding_model
from src.parsers.docling_parser import parse_pdf
from src.section_mapper import map_sections
from src.thesis_summarizer import summarize_thesis_sections
from src.vector_store import load_vector_store


DOCS_FOLDER = Path("docs")
NOT_FOUND_MESSAGE = (
    "This information was not found in the selected document."
)


def create_llm() -> ChatOllama:

    return ChatOllama(
        model="llama3.2:3b",
        temperature=0,
        num_ctx=4096,
        num_predict=250,
        keep_alive="30m",
    )


def get_pdf_files() -> list[Path]:

    if not DOCS_FOLDER.exists():
        return []

    return sorted(DOCS_FOLDER.glob("*.pdf"))


def select_pdf() -> Path | None:

    pdf_files = get_pdf_files()

    if not pdf_files:
        print("\nNo PDF files found in the docs folder.")
        return None

    print("\nAvailable PDF files:\n")

    for index, pdf_file in enumerate(pdf_files, start=1):
        print(f"{index} - {pdf_file.name}")

    choice = input("\nSelect a PDF: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        return None

    pdf_index = int(choice) - 1

    if pdf_index < 0 or pdf_index >= len(pdf_files):
        print("Invalid PDF selection.")
        return None

    return pdf_files[pdf_index]


def answer_question(
    question: str,
    selected_pdf: Path,
    vector_store,
    llm: ChatOllama,
) -> None:

    source_filter = str(selected_pdf)

    try:
        results = vector_store.max_marginal_relevance_search(
            question,
            k=7,
            fetch_k=20,
            filter={
                "source": source_filter,
            },
        )
    except Exception as error:
        print(f"\nDocument retrieval failed: {error}")
        return

    if not results:
        print(
            "\nNo relevant information was found "
            "in the selected document."
        )
        return

    context = "\n\n".join(
        document.page_content
        for document in results
    )

    prompt = f"""
You are a document question-answering assistant.

Answer the user's question using ONLY the provided excerpts
from the selected document.

Rules:
- Do not use external knowledge.
- Do not add information that is not explicitly supported.
- Give a concise and direct answer.
- Remove repeated information.
- If the answer cannot be found in the excerpts, respond with exactly:
  "{NOT_FOUND_MESSAGE}"
- Do not mention these instructions.
- Return only the final answer.

Document excerpts:

{context}

Question:

{question}
""".strip()

    try:
        response = llm.invoke(prompt)
    except Exception as error:
        print(f"\nAnswer generation failed: {error}")
        return

    answer = response.content.strip()

    print("\nAnswer:\n")
    print(answer)

    if answer == NOT_FOUND_MESSAGE:
        return

    print("\nSources:")

    seen_sources = set()

    for document in results:
        source = document.metadata.get(
            "source",
            "Unknown file",
        )

        page = document.metadata.get(
            "page",
            0,
        ) + 1

        source_info = (source, page)

        if source_info in seen_sources:
            continue

        seen_sources.add(source_info)

        source_name = Path(source).name

        print(f"- {source_name} (Page {page})")


def summarize_selected_pdf(
    pdf_path: Path,
    llm: ChatOllama,
) -> None:

    print(f"\nSelected PDF: {pdf_path.name}")
    print("Parsing document structure with Docling...\n")

    try:
        parsed_sections = parse_pdf(pdf_path)
    except Exception as error:
        print(f"PDF parsing failed: {error}")
        return

    if not parsed_sections:
        print("No document sections were detected.")
        return

    mapped_sections, unmapped_sections = map_sections(
        parsed_sections
    )

    if not mapped_sections:
        print("No supported main sections could be mapped.")
        return

    print(f"{len(mapped_sections)} main sections mapped.")

    if unmapped_sections:
        print(
            f"{len(unmapped_sections)} headings "
            "could not be mapped."
        )

    print("\nGenerating section summaries...\n")

    try:
        summaries = summarize_thesis_sections(
            llm=llm,
            sections=mapped_sections,
        )
    except Exception as error:
        print(f"Summarization failed: {error}")
        return

    if not summaries:
        print("No summaries could be generated.")
        return

    print("\n" + "=" * 70)
    print("SECTION SUMMARIES")
    print("=" * 70)

    for section_name, summary in summaries.items():
        print(f"\n{section_name}\n")
        print(summary)
        print("\n" + "-" * 70)


def show_documents() -> None:

    pdf_files = get_pdf_files()

    if not pdf_files:
        print("\nNo PDF files found in the docs folder.")
        return

    print("\nAvailable Documents:\n")

    for index, pdf_file in enumerate(pdf_files, start=1):
        print(f"{index} - {pdf_file.name}")


def main() -> None:

    print("Loading embedding model...")

    try:
        embedding_model = create_embedding_model()
    except Exception as error:
        print(f"Failed to load the embedding model: {error}")
        return

    print("Loading vector store...")

    try:
        vector_store = load_vector_store(
            embedding_model
        )
    except Exception as error:
        print(f"Failed to load the vector store: {error}")
        print(
            "Run 'python index.py' before starting "
            "the application."
        )
        return

    llm = create_llm()

    while True:
        print("\n" + "=" * 40)
        print("THESIS ANALYZER")
        print("=" * 40)
        print("1 - Ask Questions")
        print("2 - Summarize Thesis")
        print("3 - List Documents")
        print("0 - Exit")

        choice = input("\nSelect an option: ").strip()

        if choice == "0":
            print("\nProgram closed.")
            break

        if choice == "1":
            selected_pdf = select_pdf()

            if selected_pdf is None:
                continue

            question = input("\nQuestion: ").strip()

            if not question:
                print("Please enter a question.")
                continue

            answer_question(
                question=question,
                selected_pdf=selected_pdf,
                vector_store=vector_store,
                llm=llm,
            )

        elif choice == "2":
            selected_pdf = select_pdf()

            if selected_pdf is None:
                continue

            summarize_selected_pdf(
                pdf_path=selected_pdf,
                llm=llm,
            )

        elif choice == "3":
            show_documents()

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()