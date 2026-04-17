from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dishpatch.data.menu import MENU
from dishpatch.config import EMBEDDINGS_MODEL, RAG_TOP_K

def _build_documents() -> list[Document]:
    docs = []

    for item in MENU:
        tags = ', '.join(item.dietary_tags) or 'None'
        content = (
            f"{item.name} | {item.cuisine} cuisine | ${item.price} | "
            f"Rating: {item.rating} | Tags: {tags} | "
            f"{item.description}"
        )

        metadata = {
            "id": item.id,
            "name": item.name,
            "price": item.price
        }

        docs.append(Document(page_content=content, metadata=metadata))

    return docs

def build_vector_store() -> Chroma:
    embeddings = OpenAIEmbeddings(model=EMBEDDINGS_MODEL)
    docs = _build_documents()

    return Chroma.from_documents(docs, embedding=embeddings)

retriever = build_vector_store().as_retriever(search_kwargs={"k": RAG_TOP_K})