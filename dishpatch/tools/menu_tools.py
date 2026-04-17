from langchain_core.tools import tool
from dishpatch.tools.rag import retriever

@tool
def search_menu_catalog(query: str) -> str:
    """Search the DishPatch menu catalog for dishes matching the query."""
    docs = retriever.invoke(query)
    if not docs:
        return "No matching dishes found"

    return "\n\n".join(doc.page_content for doc in docs)


menu_tools_list = [search_menu_catalog]

