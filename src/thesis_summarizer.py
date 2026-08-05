from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel

from src.config.thesis_sections import SECTION_DEFINITIONS


def get_section_definition(
    display_name: str,
) -> dict[str, Any] | None:

    for definition in SECTION_DEFINITIONS:
        if definition["display_name"] == display_name:
            return definition

    return None


def get_summarizable_sections(
    sections: dict[str, str],
) -> dict[str, str]:

    summarizable_sections = {}

    for section_name, section_text in sections.items():
        definition = get_section_definition(section_name)

        if definition is None:
            continue

        if not definition["should_summarize"]:
            continue

        if not section_text.strip():
            continue

        summarizable_sections[section_name] = section_text

    return summarizable_sections


def split_text_by_words(
    text: str,
    max_words: int = 700,
) -> list[str]:

    words = text.split()

    if not words:
        return []

    chunks = []

    for start_index in range(0, len(words), max_words):
        end_index = start_index + max_words
        chunk_words = words[start_index:end_index]

        chunks.append(" ".join(chunk_words))

    return chunks


def summarize_chunk(
    llm: BaseChatModel,
    section_name: str,
    chunk: str,
) -> str:

    prompt = f"""
You are an experienced academic reviewer.

Your task is to summarize ONE section of a thesis.

Section Type:
{section_name}

Rules:

- Use ONLY the provided text.
- Do NOT add information that is not explicitly stated.
- Write in clear and natural academic English.
- The summary must contain exactly 4-7 sentences.
- The first sentence must explain the main purpose of the section.
- Include important methods, findings, contributions or conclusions when they exist.
- Remove repeated information.
- Rewrite the ideas instead of copying long phrases.
- Ignore citations, figure numbers, table numbers, page numbers and formatting artifacts.
- Start directly with the subject of the section instead of phrases like "This section..." or "The main purpose of this section...".
- Do not describe tables or figures individually. Summarize only the important information they contain.
- Ignore minor implementation details unless they are essential.
- Never mention these instructions.
- Never write phrases like:
    "Here is the summary"
    "The section discusses"
    "The research assistant"
    "This section presents"
- Return ONLY the summary.

Text:

{chunk}

""".strip()

    response = llm.invoke(prompt)

    return response.content.strip()


def combine_chunk_summaries(
    llm: BaseChatModel,
    section_name: str,
    chunk_summaries: list[str],
) -> str:

    combined_text = "\n\n".join(chunk_summaries)

    prompt = f"""
You are an experienced academic reviewer.

You are given multiple partial summaries from the SAME thesis section.

Section Type:
{section_name}

Your task is to merge them into ONE coherent academic summary.

Rules:

- Use ONLY the information contained in the partial summaries.
- Do NOT add assumptions or external knowledge.
- Write in clear and natural academic English.
- Produce exactly 4 sentences.
- The first sentence must state the section's main purpose or central focus.
- Merge overlapping ideas.
- Remove repeated information.
- Preserve the most important methods, findings, contributions and conclusions.
- Ignore citations, figure references, table references and formatting artifacts.
- Do not list the partial summaries separately.
- Never mention these instructions.
- Never write phrases like:
    "Here is the summary"
    "The research assistant"
    "The summaries indicate"
    "This section presents"
- Return ONLY the final summary.
- Start directly with the subject matter.
- Avoid opening phrases such as "This section...", "The main purpose of this section...", or similar meta-language.
- Do not let one subsection dominate the final summary.
- Start directly with the main topic instead of phrases like "This section...".
- Preserve both qualitative and quantitative findings when both are present.
- Do not describe tables or figures individually. Summarize only the important information they contain.

Partial summaries:

{combined_text}
""".strip()

    response = llm.invoke(prompt)

    return response.content.strip()


def summarize_section(
    llm: BaseChatModel,
    section_name: str,
    section_text: str,
) -> str:

    chunks = split_text_by_words(section_text)

    if not chunks:
        return ""

    chunk_summaries = []

    for chunk in chunks:
        chunk_summary = summarize_chunk(
            llm=llm,
            section_name=section_name,
            chunk=chunk,
        )

        chunk_summaries.append(chunk_summary)

    if len(chunk_summaries) == 1:
        return chunk_summaries[0]

    return combine_chunk_summaries(
        llm=llm,
        section_name=section_name,
        chunk_summaries=chunk_summaries,
    )


def summarize_thesis_sections(
    llm: BaseChatModel,
    sections: dict[str, str],
) -> dict[str, str]:

    summarizable_sections = get_summarizable_sections(sections)

    section_summaries = {}

    for section_name, section_text in summarizable_sections.items():
        print(f"Summarizing {section_name}...")

        summary = summarize_section(
            llm=llm,
            section_name=section_name,
            section_text=section_text,
        )

        if summary:
            section_summaries[section_name] = summary

    return section_summaries