import re
from typing import Any

from src.config.thesis_sections import SECTION_DEFINITIONS


def normalize_title(title: str) -> str:

    normalized = title.strip().lower()

    normalized = re.sub(
        r"^\d+(?:\.\d+)*[.)]?\s+",
        "",
        normalized,
    )

    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip(" .:-")


def get_heading_level(title: str) -> int:

    match = re.match(
        r"^(\d+(?:\.\d+)*)[.)]?\s+",
        title.strip(),
    )

    if not match:
        return 1

    return match.group(1).count(".") + 1


def is_structural_marker(title: str) -> bool:

    normalized = normalize_title(title)

    patterns = [
        r"chapter\s+[ivxlcdm]+",
        r"chapter\s+\d+",
        r"part\s+[ivxlcdm]+",
        r"part\s+\d+",
        r"section\s+[a-z]",
        r"section\s+\d+",
        r"bölüm\s+[ivxlcdm]+",
        r"bölüm\s+\d+",
        r"kısım\s+[ivxlcdm]+",
        r"kısım\s+\d+",
    ]

    return any(
        re.fullmatch(pattern, normalized)
        for pattern in patterns
    )


def get_definition_by_key(
    section_key: str,
) -> dict[str, Any] | None:

    for definition in SECTION_DEFINITIONS:
        if definition["key"] == section_key:
            return definition

    return None


def find_exact_definition(
    normalized_title: str,
) -> dict[str, Any] | None:

    for definition in SECTION_DEFINITIONS:
        normalized_aliases = {
            normalize_title(alias)
            for alias in definition["aliases"]
        }

        if normalized_title in normalized_aliases:
            return definition

    return None


def find_prefix_definition(
    normalized_title: str,
) -> dict[str, Any] | None:
   
    prefix_patterns = {
        "abstract": [
            r"^abstract(?:\s*[:\-]\s*|\s+)",
            r"^özet(?:\s*[:\-]\s*|\s+)",
        ],
        "introduction": [
            r"^introduction(?:\s*[:\-]\s*|\s+)",
            r"^general introduction(?:\s*[:\-]\s*|\s+)",
            r"^giriş(?:\s*[:\-]\s*|\s+)",
        ],
        "literature_review": [
            r"^literature review(?:\s*[:\-]\s*|\s+)",
            r"^review of literature(?:\s*[:\-]\s*|\s+)",
            r"^related works?(?:\s*[:\-]\s*|\s+)",
            r"^background(?:\s*[:\-]\s*|\s+)",
            r"^overview(?:\s*[:\-]\s*|\s+)",
            r"^literatür (?:taraması|incelemesi)(?:\s*[:\-]\s*|\s+)",
        ],
        "methodology": [
            r"^methodology(?:\s*[:\-]\s*|\s+)",
            r"^methods?(?:\s*[:\-]\s*|\s+)",
            r"^materials? and methods?(?:\s*[:\-]\s*|\s+)",
            r"^research methodology(?:\s*[:\-]\s*|\s+)",
            r"^research methods?(?:\s*[:\-]\s*|\s+)",
            r"^experimental procedures?(?:\s*[:\-]\s*|\s+)",
            r"^study design(?:\s*[:\-]\s*|\s+)",
            r"^user analysis(?:\s*[:\-]\s*|\s+)",
            r"^participant analysis(?:\s*[:\-]\s*|\s+)",
            r"^understanding user diversity(?:\s*[:\-]\s*|\s+)",
            r"^materyal ve (?:metot|yöntem)(?:\s*[:\-]\s*|\s+)",
            r"^gereç ve yöntem(?:\s*[:\-]\s*|\s+)",
        ],
        "results": [
            r"^results?(?:\s*[:\-]\s*|\s+(?:and|of|from)\s+)",
            r"^findings?(?:\s*[:\-]\s*|\s+(?:and|of|from)\s+)",
            r"^experimental results?(?:\s*[:\-]\s*|\s+)",
            r"^bulgular(?:\s*[:\-]\s*|\s+(?:ve|ile)\s+)",
            r"^deneysel sonuçlar(?:\s*[:\-]\s*|\s+)",
        ],
        "discussion": [
            r"^discussion(?:\s*[:\-]\s*|\s+(?:and|of|on)\s+)",
            r"^general discussion(?:\s*[:\-]\s*|\s+)",
            r"^requirements? proposal(?:\s*[:\-]\s*|\s+)",
            r"^proposed requirements?(?:\s*[:\-]\s*|\s+)",
            r"^requirement framework(?:\s*[:\-]\s*|\s+)",
            r"^tartışma(?:\s*[:\-]\s*|\s+(?:ve|üzerine)\s+)",
            r"^değerlendirme(?:\s*[:\-]\s*|\s+)",
        ],
        "conclusion": [
            r"^conclusions?(?:\s*[:\-]\s*|\s+(?:and|of|from)\s+)",
            r"^summary and conclusions?(?:\s*[:\-]\s*|\s+)",
            r"^general conclusions?(?:\s*[:\-]\s*|\s+)",
            r"^sonuçlar?(?:\s*[:\-]\s*|\s+(?:ve|ile)\s+)",
        ],
        "future_work": [
            r"^future work(?:\s*[:\-]\s*|\s+)",
            r"^future studies(?:\s*[:\-]\s*|\s+)",
            r"^future research(?:\s*[:\-]\s*|\s+)",
            r"^future directions(?:\s*[:\-]\s*|\s+)",
            r"^recommendations?(?:\s*[:\-]\s*|\s+)",
            r"^recommendations? for future (?:studies|research)(?:\s*[:\-]\s*|\s+)",
            r"^gelecek çalışmalar(?:\s*[:\-]\s*|\s+)",
            r"^öneriler(?:\s*[:\-]\s*|\s+)",
        ],
        "references": [
            r"^references?(?:\s*[:\-]\s*|\s+)",
            r"^references cited(?:\s*[:\-]\s*|\s+)",
            r"^bibliography(?:\s*[:\-]\s*|\s+)",
            r"^kaynaklar(?:\s*[:\-]\s*|\s+)",
            r"^kaynakça(?:\s*[:\-]\s*|\s+)",
        ],
        "appendix": [
            r"^appendix(?:\s*[:\-]\s*|\s+)",
            r"^appendices(?:\s*[:\-]\s*|\s+)",
            r"^supplementary materials?(?:\s*[:\-]\s*|\s+)",
            r"^ekler?(?:\s*[:\-]\s*|\s+)",
        ],
    }

    for section_key, patterns in prefix_patterns.items():
        for pattern in patterns:
            if re.match(pattern, normalized_title):
                return get_definition_by_key(section_key)

    return None


def append_content(
    mapped_sections: dict[str, str],
    section_name: str,
    content: str,
) -> None:

    existing_content = mapped_sections.get(
        section_name,
        "",
    )

    mapped_sections[section_name] = (
        f"{existing_content}\n\n{content}".strip()
    )


def map_sections(
    parsed_sections: list[dict],
) -> tuple[dict[str, str], list[dict]]:

    mapped_sections: dict[str, str] = {}
    unmapped_sections: list[dict] = []

    current_main_section: str | None = None

    for section in parsed_sections:
        raw_title = section.get(
            "title",
            "",
        ).strip()

        content = section.get(
            "content",
            "",
        ).strip()

        if not raw_title:
            continue

        if is_structural_marker(raw_title):
            continue

        if not content:
            continue

        heading_level = section.get(
            "markdown_level",
            get_heading_level(raw_title),
        )

        normalized_title = normalize_title(raw_title)

        definition = find_exact_definition(
            normalized_title
        )

        if definition is None:
            definition = find_prefix_definition(
                normalized_title
            )

        if definition is not None:
            current_main_section = definition["display_name"]

            if definition["should_summarize"]:
                append_content(
                    mapped_sections=mapped_sections,
                    section_name=current_main_section,
                    content=content,
                )

            continue

        if heading_level > 1 and current_main_section is not None:
            if current_main_section in mapped_sections:
                subsection_content = (
                    f"{raw_title}\n\n{content}"
                )

                append_content(
                    mapped_sections=mapped_sections,
                    section_name=current_main_section,
                    content=subsection_content,
                )

            continue

        unmapped_sections.append(
            {
                "title": raw_title,
                "content_preview": content[:150],
                "heading_level": heading_level,
            }
        )

    return mapped_sections, unmapped_sections
