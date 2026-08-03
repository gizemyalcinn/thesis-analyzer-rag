import re
from typing import Any

from src.config.thesis_sections import SECTION_DEFINITIONS


def normalize_title(title: str) -> str:
    

    normalized = title.strip().lower()

    normalized = re.sub(
        r"^\d+(?:\.\d+)*\s+",
        "",
        normalized,
    )

    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip(" .:-")


def get_heading_level(title: str) -> int:

    match = re.match(
        r"^(\d+(?:\.\d+)*)\s+",
        title.strip(),
    )

    if not match:
        return 1

    return match.group(1).count(".") + 1


def find_exact_definition(
    normalized_title: str,
) -> dict[str, Any] | None:

    for definition in SECTION_DEFINITIONS:
        aliases = {
            normalize_title(alias)
            for alias in definition["aliases"]
        }

        if normalized_title in aliases:
            return definition

    return None
def find_prefix_definition(
    normalized_title: str,
) -> dict[str, Any] | None:

    prefix_patterns = {
        "abstract": [
            r"^abstract(?:\s*[:\-]\s*|\s+)",
        ],
        "introduction": [
            r"^introduction(?:\s*[:\-]\s*|\s+)",
            r"^giriş(?:\s*[:\-]\s*|\s+)",
        ],
        "overview": [
            r"^overview(?:\s*[:\-]\s*|\s+)",
            r"^background(?:\s*[:\-]\s*|\s+)",
        ],
        "user_analysis": [
            r"^understanding user diversity(?:\s*[:\-]\s*|\s+)",
            r"^user analysis(?:\s*[:\-]\s*|\s+)",
        ],
        "results": [
            r"^results(?:\s*[:\-]\s*|\s+(?:and|of|from)\s+)",
            r"^findings(?:\s*[:\-]\s*|\s+(?:and|of|from)\s+)",
            r"^bulgular(?:\s*[:\-]\s*|\s+(?:ve|ile)\s+)",
        ],
        "discussion": [
            r"^discussion(?:\s*[:\-]\s*|\s+(?:and|of|on)\s+)",
            r"^tartışma(?:\s*[:\-]\s*|\s+(?:ve|üzerine)\s+)",
        ],
        "requirements": [
            r"^requirements?(?:\s*[:\-]\s*|\s+(?:proposal|framework|analysis)\b)",
            r"^gereksinimler?(?:\s*[:\-]\s*|\s+(?:önerisi|çerçevesi)\b)",
        ],
        "conclusion": [
            r"^conclusions?(?:\s*[:\-]\s*|\s+(?:and|of|from)\s+)",
            r"^sonuçlar?(?:\s*[:\-]\s*|\s+(?:ve|ile)\s+)",
        ],
    }

    for section_key, patterns in prefix_patterns.items():
        for pattern in patterns:
            if re.match(pattern, normalized_title):
                for definition in SECTION_DEFINITIONS:
                    if definition["key"] == section_key:
                        return definition

    return None

def map_sections(
    parsed_sections: list[dict],
) -> tuple[dict[str, str], list[dict]]:

    mapped_sections = {}
    unmapped_sections = []

    current_main_section = None

    for section in parsed_sections:
        raw_title = section["title"]
        content = section["content"].strip()

        if not content:
            continue

        heading_level = get_heading_level(raw_title)
        normalized_title = normalize_title(raw_title)

        definition = find_exact_definition(normalized_title)

        if definition is None:
            definition = find_prefix_definition(normalized_title)

        if definition is not None:
            current_main_section = definition["display_name"]

            if definition["should_summarize"]:
                existing_content = mapped_sections.get(
                    current_main_section,
                    "",
                )

                mapped_sections[current_main_section] = (
                    f"{existing_content}\n\n{content}".strip()
                )

            continue

        if heading_level > 1 and current_main_section is not None:
            if current_main_section in mapped_sections:
                subsection_text = (
                    f"{raw_title}\n\n{content}"
                )

                mapped_sections[current_main_section] = (
                    f"{mapped_sections[current_main_section]}"
                    f"\n\n{subsection_text}"
                ).strip()

            continue

        unmapped_sections.append(
            {
                "title": raw_title,
                "content_preview": content[:150],
                "heading_level": heading_level,
            }
        )

    return mapped_sections, unmapped_sections