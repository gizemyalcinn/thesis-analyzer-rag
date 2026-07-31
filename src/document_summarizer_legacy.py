import re
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def get_pdf_files(docs_path="docs"):
    """
    docs klasöründeki bütün PDF dosyalarını döndürür.
    """

    docs_folder = Path(docs_path)

    if not docs_folder.exists():
        return []

    return sorted(docs_folder.glob("*.pdf"))


def create_pdf_chunks(pdf_path):
    """
    PDF dosyasını yükler ve metni chunk'lara ayırır.
    """

    loader = PyPDFLoader(str(pdf_path))
    pages = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1200,
        chunk_overlap=150,
        separators=[
            "\n\n",
            "\n",
            ". ",
            " ",
            ""
        ]
    )

    chunks = text_splitter.split_documents(pages)

    return chunks


def is_relevant_chunk(chunk):
    """
    Kapak, jüri, etik beyan ve içindekiler gibi
    özet açısından düşük değerli chunk'ları filtreler.
    """

    text = chunk.page_content.strip()
    normalized_text = text.lower()

    if len(text) < 150:
        return False

    low_value_markers = [
        "etik beyan",
        "etik bildirim",
        "bilimsel etiğe uygun",
        "jüri üyesi",
        "danışman",
        "tez danışmanı",
        "tez onay",
        "onay sayfası",
        "imza",
        "içindekiler",
        "şekiller listesi",
        "tablolar listesi",
        "kısaltmalar listesi",
        "semboller listesi",
        "özgeçmiş",
        "teşekkür",
        "telif hakkı",
        "lisans bitirme tezi",
        "yüksek lisans tezi",
        "doktora tezi",
        "fen bilimleri enstitüsü",
        "sosyal bilimler enstitüsü",
        "oy birliği",
        "oy çokluğu",
        "savunma sınavı",
        "kabul edilmiştir"
    ]

    meaningful_markers = [
        "amaç",
        "problem",
        "yöntem",
        "metodoloji",
        "uygulama",
        "sistem",
        "model",
        "veri seti",
        "veriseti",
        "eğitim",
        "test",
        "bulgu",
        "sonuç",
        "mimari",
        "algoritma",
        "donanım",
        "yazılım",
        "performans",
        "doğruluk",
        "başarı",
        "analiz",
        "tasarım",
        "geliştirme",
        "deney",
        "değerlendirme",
        "öneri",
        "karşılaştırma"
    ]

    low_value_score = sum(
        marker in normalized_text
        for marker in low_value_markers
    )

    meaningful_score = sum(
        marker in normalized_text
        for marker in meaningful_markers
    )

    table_of_contents_matches = re.findall(
        r"\.{3,}\s*\d+",
        text
    )

    page_number_lines = re.findall(
        r"^\s*\d+\s*$",
        text,
        flags=re.MULTILINE
    )

    if len(table_of_contents_matches) >= 2:
        return False

    if low_value_score >= 2 and meaningful_score == 0:
        return False

    if low_value_score >= 3 and meaningful_score <= 1:
        return False

    if len(page_number_lines) >= 5 and meaningful_score == 0:
        return False

    return True


def group_items(items, group_size):
    """
    Bir listeyi belirtilen büyüklükte gruplara ayırır.
    """

    return [
        items[index:index + group_size]
        for index in range(0, len(items), group_size)
    ]


def clean_model_response(response_content):
    """
    Model cevabındaki gereksiz başlık ve boşlukları temizler.
    """

    text = response_content.strip()

    unwanted_prefixes = [
        "özet:",
        "ara özet:",
        "ara özetler:",
        "birleştirilmiş özet:",
        "nihai özet:"
    ]

    normalized_text = text.lower()

    for prefix in unwanted_prefixes:
        if normalized_text.startswith(prefix):
            text = text[len(prefix):].strip()
            break

    return text


def summarize_chunk_group(chunk_group, llm):
    """
    Birden fazla chunk'ı tek model çağrısıyla ara özete dönüştürür.
    """

    group_text = "\n\n".join(
        chunk.page_content.strip()
        for chunk in chunk_group
        if chunk.page_content.strip()
    )

    prompt = f"""
GÖREV:
Aşağıdaki belge parçalarındaki temel ve anlamlı bilgileri Türkçe özetle.

KURALLAR:
1. Yalnızca verilen belge parçalarındaki bilgileri kullan.
2. Belgenin ana fikrine katkı sağlayan bilgileri öne çıkar.
3. Amaç, problem, yöntem, süreç, uygulama, bulgu ve sonuçları varsa koru.
4. Önemli teknik kavramları, teknolojileri ve yöntemleri atlama.
5. Kapak bilgilerini, üniversite adını, yazar listesini, danışmanı, jüri üyelerini ve tarihleri yazma.
6. Etik beyan, imza, onay, teşekkür, içindekiler ve liste sayfalarını özetleme.
7. Sayfa, şekil, tablo ve bölüm numaralarını gereksiz yere yazma.
8. Aynı bilgiyi tekrar etme.
9. Belgede bulunmayan bilgi ekleme veya tahmin yapma.
10. Başına "Ara Özet", "Özet" veya benzeri bir ifade yazma.
11. Doğrudan özet metniyle başla.

BELGE PARÇALARI:
{group_text}
"""

    response = llm.invoke(prompt)

    return clean_model_response(response.content)


def combine_summary_group(summary_group, llm, final_stage=False):
    """
    Birden fazla ara özeti daha kapsamlı tek bir özette birleştirir.
    """

    summaries_text = "\n\n---\n\n".join(
        summary.strip()
        for summary in summary_group
        if summary.strip()
    )

    if final_stage:
        task_description = """
Aşağıdaki ara özetleri kullanarak belgenin nihai ve bütünlüklü özetini oluştur.
Belgenin içeriğine uygun başlıklar kullanabilirsin.
"""
    else:
        task_description = """
Aşağıdaki ara özetleri daha kısa, bütünlüklü ve kapsamlı bir ara özette birleştir.
Bu aşamada gereksiz başlıklar oluşturma.
"""

    prompt = f"""
GÖREV:
{task_description}

KURALLAR:
1. Yalnızca verilen ara özetlerde bulunan bilgileri kullan.
2. Belgenin ana amacı ve temel konusu açıkça anlaşılmalı.
3. Önemli yöntemleri, süreçleri, teknolojileri, bulguları ve sonuçları koru.
4. Önemsiz idari bilgileri, kişi listelerini ve tarihleri dahil etme.
5. Aynı bilgileri tekrar etme.
6. Birbiriyle ilişkili bilgileri aynı bölümde birleştir.
7. Belgede bulunmayan bilgi ekleme veya tahmin yapma.
8. Metni açık, doğal ve anlaşılır Türkçe ile yaz.
9. Başına "Ara Özetler", "Birleştirilmiş Özet" veya "Nihai Özet" yazma.
10. Numaralandırılmış ara özet listesi oluşturma.
11. Doğrudan belge özetiyle başla.

ARA ÖZET METİNLERİ:
{summaries_text}
"""

    response = llm.invoke(prompt)

    return clean_model_response(response.content)


def summarize_pdf(pdf_path, llm):
    """
    PDF'yi chunk tabanlı ve çok aşamalı şekilde özetler.
    """

    print("\nPDF okunuyor ve chunk'lara ayrılıyor...")

    try:
        chunks = create_pdf_chunks(pdf_path)
    except Exception as error:
        return f"PDF okunurken bir hata oluştu: {error}"

    if not chunks:
        return "PDF içerisinde özetlenebilir bir metin bulunamadı."

    print(f"Toplam {len(chunks)} chunk oluşturuldu.")

    relevant_chunks = [
        chunk
        for chunk in chunks
        if is_relevant_chunk(chunk)
    ]

    filtered_count = len(chunks) - len(relevant_chunks)

    print(f"{filtered_count} düşük değerli chunk filtrelendi.")
    print(f"{len(relevant_chunks)} anlamlı chunk özetlenecek.")

    if not relevant_chunks:
        return "PDF içerisinde anlamlı bir içerik bulunamadı."

    chunk_groups = group_items(
        relevant_chunks,
        group_size=3
    )

    summaries = []

    print(
        f"\nİlk özetleme aşaması başladı. "
        f"Toplam {len(chunk_groups)} grup işlenecek."
    )

    for index, chunk_group in enumerate(
        chunk_groups,
        start=1
    ):
        try:
            summary = summarize_chunk_group(
                chunk_group,
                llm
            )

            if summary:
                summaries.append(summary)

            print(
                f"Chunk grubu "
                f"{index}/{len(chunk_groups)} özetlendi."
            )

        except Exception as error:
            print(
                f"Chunk grubu {index} özetlenirken "
                f"hata oluştu: {error}"
            )

    if not summaries:
        return "Belge özetlenirken geçerli bir ara özet oluşturulamadı."

    level = 1

    while len(summaries) > 1:
        summary_groups = group_items(
            summaries,
            group_size=3
        )

        print(
            f"\nÖzet birleştirme seviyesi {level} başladı. "
            f"{len(summary_groups)} grup işlenecek."
        )

        new_summaries = []

        for index, summary_group in enumerate(
            summary_groups,
            start=1
        ):
            try:
                is_final_stage = len(summary_groups) == 1

                combined_summary = combine_summary_group(
                    summary_group,
                    llm,
                    final_stage=is_final_stage
                )

                if combined_summary:
                    new_summaries.append(combined_summary)

                print(
                    f"Özet grubu "
                    f"{index}/{len(summary_groups)} birleştirildi."
                )

            except Exception as error:
                print(
                    f"Özet grubu {index} birleştirilirken "
                    f"hata oluştu: {error}"
                )

        if not new_summaries:
            return "Ara özetler birleştirilirken bir hata oluştu."

        summaries = new_summaries
        level += 1

    return summaries[0]