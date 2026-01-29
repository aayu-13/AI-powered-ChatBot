from bs4 import BeautifulSoup
from langchain_community.document_loaders import WebBaseLoader

def crawl_and_clean(url: str):
    """Crawl website and extract clean textual content."""
    loader = WebBaseLoader(url)
    loader.bs_get_text_kwargs = {"strip": True}
    docs = loader.load()

    if not docs:
        return []

    cleaned_docs = []

    for doc in docs:
        soup = BeautifulSoup(doc.page_content, "html.parser")

        for tag in soup([
            "nav", "header", "footer", "script",
            "style", "aside", "form"
        ]):
            tag.decompose()

        text = soup.get_text(separator=" ").strip()

        if text:
            doc.page_content = text
            cleaned_docs.append(doc)

    return cleaned_docs
