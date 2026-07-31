import re
import unicodedata
from typing import Any

from langchain_core.documents import Document

from src.config.thesis_sections import SECTION_DEFINITIONS


def normalize_text(text: str) -> str:
    """PDF metnindeki görünmez karakterleri ve fazla boşlukları temizler."""

    normalized = unicodedata.normalize("NFKC", text)

    normalized = normalized.replace("\u00a0", " ")
    normalized = normalized.replace("\u200b", "")
    normalized = normalized.replace("\ufeff", "")

    normalized = re.sub(r"\s+", " ", normalized)

    return normalized.strip()


def extract_heading_number(line: str) -> int | None:
    """
    Ana bölüm numarasını çıkarır.

    Örnek:
    '1 Introduction' -> 1
    '2. Overview' -> 2
    '3) Method' -> 3
    '3.1 Participants' -> None
    """

    normalized = normalize_text(line)

    match = re.match(
        r"^\s*(\d+)(?:[.)])?\s+",
        normalized,
    )

    if not match:
        return None

    return int(match.group(1))

def remove_heading_number(line: str) -> str:
    """Başlığın başındaki ana bölüm numarasını kaldırır."""

    normalized = normalize_text(line)

    normalized = re.sub(
        r"^\s*\d+(?:[.)])?\s+",
        "",
        normalized,
    )

    return normalized.strip(" .:;-")

def normalize_heading(line: str) -> str:
    """Başlığı karşılaştırmaya uygun hâle getirir."""

    heading = remove_heading_number(line)
    heading = heading.lower()

    return heading.strip()


def is_toc_line(line: str) -> bool:
    """Satırın İçindekiler bölümüne ait olup olmadığını kontrol eder."""

    normalized = normalize_text(line)

    if re.search(r"\.{3,}", normalized):
        return True

    if re.search(r"\s+\d+\s*$", normalized) and "." in normalized:
        return True

    return False


def is_possible_heading(line: str) -> bool:
    """Satırın gerçek bir bölüm başlığına benzeyip benzemediğini kontrol eder."""

    normalized = normalize_text(line)

    if not normalized:
        return False

    if len(normalized) > 100:
        return False

    if len(normalized.split()) > 10:
        return False

    if is_toc_line(normalized):
        return False

    return True


def get_definition_by_key(
    section_key: str,
) -> dict[str, Any] | None:
    """Bölüm anahtarına karşılık gelen tanımı döndürür."""

    for definition in SECTION_DEFINITIONS:
        if definition["key"] == section_key:
            return definition

    return None


def detect_section_candidates(
    line: str,
) -> list[dict[str, Any]]:
    """Bir satırla eşleşen olası bölüm tanımlarını döndürür."""

    if not is_possible_heading(line):
        return []

    normalized_heading = normalize_heading(line)
    heading_number = extract_heading_number(line)

    candidates = []

    for definition in SECTION_DEFINITIONS:
        aliases = {
            normalize_text(alias).lower()
            for alias in definition["aliases"]
        }

        if normalized_heading not in aliases:
            continue

        requires_number = definition["requires_number"]

        if requires_number and heading_number is None:
            continue

        candidate = definition.copy()
        candidate["heading_number"] = heading_number

        candidates.append(candidate)

    return candidates


def choose_section_candidate(
    candidates: list[dict[str, Any]],
    previous_section_key: str | None,
) -> dict[str, Any] | None:
    """
    Birden fazla bölüm eşleşmesi varsa tez sırasına göre en uygun olanı seçer.
    """

    if not candidates:
        return None

    if len(candidates) == 1:
        return candidates[0]

    if previous_section_key is None:
        return min(
            candidates,
            key=lambda item: item["order"],
        )

    previous_definition = get_definition_by_key(
        previous_section_key
    )

    if previous_definition is None:
        return candidates[0]

    previous_order = previous_definition["order"]

    later_candidates = [
        candidate
        for candidate in candidates
        if candidate["order"] >= previous_order
    ]

    if later_candidates:
        return min(
            later_candidates,
            key=lambda item: item["order"],
        )

    return max(
        candidates,
        key=lambda item: item["order"],
    )


def detect_section_heading(
    line: str,
    previous_section_key: str | None = None,
) -> dict[str, Any] | None:
    """Bir satırın hangi tez bölümüne ait olduğunu belirler."""

    candidates = detect_section_candidates(line)

    return choose_section_candidate(
        candidates=candidates,
        previous_section_key=previous_section_key,
    )


def find_section_starts(
    documents: list[Document],
) -> list[dict[str, Any]]:
    """Ana bölümlerin gerçek PDF başlangıçlarını bulur."""

    section_starts = []
    found_keys = set()
    previous_section_key = None

    for page_index, document in enumerate(documents):
        lines = [
            normalize_text(line)
            for line in document.page_content.splitlines()
            if normalize_text(line)
        ]

        # Ana bölüm başlıkları çoğunlukla sayfanın ilk kısmında olur.
        for line_index, line in enumerate(lines[:20]):
            detected = detect_section_heading(
                line=line,
                previous_section_key=previous_section_key,
            )

            if detected is None:
                continue

            section_key = detected["key"]

            if section_key in found_keys:
                continue

            section_starts.append(
                {
                    "key": section_key,
                    "display_name": detected["display_name"],
                    "order": detected["order"],
                    "page_index": page_index,
                    "line_index": line_index,
                }
            )

            found_keys.add(section_key)
            previous_section_key = section_key

            break

    return section_starts


def clean_section_text(
    text: str,
) -> str:
    """Bölüm metnindeki gereksiz satırları temizler."""

    cleaned_lines = []

    for raw_line in text.splitlines():
        line = normalize_text(raw_line)

        if not line:
            continue

        # Tek başına duran sayfa numaralarını kaldırır.
        if re.fullmatch(r"[ivxlcdm]+|\d+", line.lower()):
            continue

        # İçindekiler satırlarını kaldırır.
        if is_toc_line(line):
            continue

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines).strip()


def collect_section_text(
    documents: list[Document],
    start_page: int,
    end_page: int,
    section_key: str,
) -> str:
    """İki ana bölüm arasındaki metni toplar."""

    collected_lines = []
    is_first_page = True
    heading_skipped = False

    for page_index in range(start_page, end_page):
        document = documents[page_index]

        lines = document.page_content.splitlines()

        for raw_line in lines:
            line = normalize_text(raw_line)

            if not line:
                continue

            if is_first_page and not heading_skipped:
                detected = detect_section_heading(line)

                if (
                    detected is not None
                    and detected["key"] == section_key
                ):
                    heading_skipped = True
                    continue

            collected_lines.append(line)

        is_first_page = False

    section_text = "\n".join(collected_lines)

    return clean_section_text(section_text)


def extract_thesis_sections(
    documents: list[Document],
) -> dict[str, str]:
    """Tezin ana bölümlerini bulur ve metinlerini ayrı ayrı çıkarır."""

    section_starts = find_section_starts(documents)

    if not section_starts:
        raise ValueError(
            "PDF içerisinde desteklenen ana tez başlıkları bulunamadı."
        )

    extracted_sections = {}

    for index, section in enumerate(section_starts):
        start_page = section["page_index"]

        if index + 1 < len(section_starts):
            end_page = section_starts[index + 1]["page_index"]
        else:
            end_page = len(documents)

        section_text = collect_section_text(
            documents=documents,
            start_page=start_page,
            end_page=end_page,
            section_key=section["key"],
        )

        if section_text:
            extracted_sections[
                section["display_name"]
            ] = section_text

    return extracted_sections