from typing import Any

from langchain_core.language_models.chat_models import BaseChatModel

from src.config.thesis_sections import SECTION_DEFINITIONS


def get_section_definition(
    display_name: str,
) -> dict[str, Any] | None:
    """Görünen bölüm adına karşılık gelen yapılandırmayı bulur."""

    for definition in SECTION_DEFINITIONS:
        if definition["display_name"] == display_name:
            return definition

    return None


def get_summarizable_sections(
    sections: dict[str, str],
) -> dict[str, str]:
    """Özetlenmesi gereken tez bölümlerini seçer."""

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
    max_words: int = 1200,
) -> list[str]:
    """Uzun bölüm metnini kelime sınırına göre parçalara ayırır."""

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
    """Bir bölüm parçasını kısa ve akademik biçimde özetler."""

    prompt = f"""
Aşağıdaki metin "{section_name}" adlı akademik tez bölümünden alınmıştır.

Metni Türkçe olarak özetle.

Kurallar:
- Yalnızca verilen metindeki bilgilere dayan.
- Metinde bulunmayan bilgi ekleme.
- Akademik fakat anlaşılır bir dil kullan.
- Ana amaçları, yöntemleri, bulguları veya çıkarımları koru.
- Tekrarları çıkar.
- 3 ile 5 cümle arasında yaz.
- Başlık ekleme.

Metin:
{chunk}
""".strip()

    response = llm.invoke(prompt)

    return response.content.strip()


def combine_chunk_summaries(
    llm: BaseChatModel,
    section_name: str,
    chunk_summaries: list[str],
) -> str:
    """Parça özetlerini tek ve tutarlı bölüm özetine dönüştürür."""

    combined_text = "\n\n".join(chunk_summaries)

    prompt = f"""
Aşağıda "{section_name}" adlı tez bölümünün parça özetleri bulunmaktadır.

Bu parça özetlerini tek ve bütünlüklü bir bölüm özetine dönüştür.

Kurallar:
- Yalnızca verilen özetlerdeki bilgileri kullan.
- Aynı bilgileri tekrar etme.
- Önemli teknik ayrıntıları koru.
- Akademik fakat anlaşılır bir Türkçe kullan.
- 3 ile 5 cümle arasında yaz.
- Başlık ekleme.

Parça özetleri:
{combined_text}
""".strip()

    response = llm.invoke(prompt)

    return response.content.strip()


def summarize_section(
    llm: BaseChatModel,
    section_name: str,
    section_text: str,
) -> str:
    """Bir tez bölümünü gerektiğinde parçalara ayırarak özetler."""

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
    """Özetlenebilir tüm tez bölümlerini ayrı ayrı özetler."""

    summarizable_sections = get_summarizable_sections(sections)

    section_summaries = {}

    for section_name, section_text in summarizable_sections.items():
        print(f"{section_name} bölümü özetleniyor...")

        summary = summarize_section(
            llm=llm,
            section_name=section_name,
            section_text=section_text,
        )

        if summary:
            section_summaries[section_name] = summary

    return section_summaries