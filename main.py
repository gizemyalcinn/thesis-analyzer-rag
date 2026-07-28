from langchain_ollama import ChatOllama

from src.embedding_model import create_embedding_model
from src.vector_store import load_vector_store


embedding_model = create_embedding_model()
vector_store = load_vector_store(embedding_model)

llm = ChatOllama(
    model="llama3.2:3b",
    keep_alive="30m",
    num_ctx=2048,
    num_predict=200,
    temperature=0
)

while True:
    question = input("\nSorunuz ('bye' yazarak kapatın): ")

    if question.lower() == "bye":
        print("Program kapatıldı.")
        break

    results = vector_store.max_marginal_relevance_search(
    question,
    k=7,
    fetch_k=20
    )

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
3. Cevabı doğrudan ver.
4. Bilgi yoksa yalnızca "Bu bilgi belgelerde bulunamadı." yaz.
5. Cevabı Türkçe, kısa ve doğal yaz.
6. Belge parçalarında geçen tüm özel teknoloji, araç, framework, model, platform ve donanım adlarını eksiksiz listele.
7. Donanım, yazılım, yapay zekâ ve veri altyapısı olarak gruplandır.


Belge parçaları:
{context}

Soru:
{question}
"""

    response = llm.invoke(prompt)

    print("\nCevap:\n")
    print(response.content)

    print("\nKaynaklar:")

    seen_sources = set()

    for document in results:
        source = document.metadata.get("source", "Bilinmeyen dosya")
        page = document.metadata.get("page", 0) + 1

        source_info = (source, page)

        if source_info not in seen_sources:
            seen_sources.add(source_info)
            print(f"- {source} (Sayfa {page})")