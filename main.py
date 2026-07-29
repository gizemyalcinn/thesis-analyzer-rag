from langchain_ollama import ChatOllama

from src.document_summarizer import get_pdf_files, summarize_pdf
from src.embedding_model import create_embedding_model
from src.vector_store import load_vector_store


def answer_question(question, vector_store, llm):
    results = vector_store.max_marginal_relevance_search(
        question,
        k=7,
        fetch_k=20
    )

    for document in results:
        print("\n--- Bulunan chunk ---")
        print(document.page_content)

    context = "\n\n".join(
        document.page_content
        for document in results
    )

    prompt = f"""
GÖREV:
Aşağıdaki belge parçalarına dayanarak kullanıcının sorusunu cevapla.

KURALLAR:
1. Sadece belge parçalarındaki bilgileri kullan.
2. Kurallardan veya görev tanımından bahsetme.
3. Cevabı doğrudan, kısa ve Türkçe ver.
4. Belgede bulunmayan hiçbir bilgi ekleme veya tahmin yapma.
5. Aynı bilgiyi tekrar etme.
6. Soruyla ilgisiz şekil, tablo ve bölüm numaralarını yazma.
7. Bilgi yoksa yalnızca "Bu bilgi belgelerde bulunamadı." yaz.

BELGE PARÇALARI:
{context}

KULLANICI SORUSU:
{question}

CEVAP:
"""

    response = llm.invoke(prompt)

    print("\nCevap:\n")
    print(response.content)

    print("\nKaynaklar:")

    seen_sources = set()

    for document in results:
        source = document.metadata.get(
            "source",
            "Bilinmeyen dosya"
        )

        page = document.metadata.get(
            "page",
            0
        ) + 1

        source_info = (source, page)

        if source_info not in seen_sources:
            seen_sources.add(source_info)
            print(f"- {source} (Sayfa {page})")


embedding_model = create_embedding_model()

vector_store = load_vector_store(
    embedding_model
)

llm = ChatOllama(
    model="llama3.2:3b",
    keep_alive="30m",
    num_ctx=2048,
    num_predict=200,
    temperature=0
)

while True:
    print("\n==============================")
    print("Local Docs RAG")
    print("==============================")
    print("1 - Belgelerde soru sor")
    print("2 - PDF özetle")
    print("0 - Çıkış")

    choice = input("\nSeçiminiz: ").strip()

    if choice == "0":
        print("Program kapatıldı.")
        break

    elif choice == "1":
        question = input("\nSorunuz: ").strip()

        if not question:
            print("Lütfen bir soru yazın.")
            continue

        answer_question(
            question,
            vector_store,
            llm
        )

    elif choice == "2":
        pdf_files = get_pdf_files()

        if not pdf_files:
            print("\ndocs klasöründe PDF bulunamadı.")
            continue

        print("\nPDF dosyaları:")

        for index, pdf_file in enumerate(
            pdf_files,
            start=1
        ):
            print(f"{index} - {pdf_file.name}")

        pdf_choice = input(
            "\nÖzetlenecek PDF numarası: "
        ).strip()

        if not pdf_choice.isdigit():
            print("Lütfen geçerli bir sayı girin.")
            continue

        pdf_index = int(pdf_choice) - 1

        if pdf_index < 0 or pdf_index >= len(pdf_files):
            print("Geçersiz PDF seçimi.")
            continue

        selected_pdf = pdf_files[pdf_index]

        print(
            f"\n{selected_pdf.name} özetleniyor..."
        )

        summary = summarize_pdf(
            selected_pdf,
            llm
        )

        print("\n==============================")
        print("PDF Özeti")
        print("==============================")
        print(summary)

    else:
        print("Geçersiz seçim.")