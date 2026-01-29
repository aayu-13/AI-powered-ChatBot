import streamlit as st
import os

from utils import validate_url
from crawler import crawl_and_clean
from embeddings_store import create_vectorstore
from qa_chain import build_qa_chain

st.set_page_config(page_title="AI Website Chatbot")
st.title("♊ AI Website Chatbot")

st.write("Ask questions **strictly based on website content**.")

api_key = st.sidebar.text_input("Enter Google API Key", type="password")

if not api_key:
    st.info("Please enter your Google API key to continue.")
    st.stop()

os.environ["GOOGLE_API_KEY"] = api_key

url = st.text_input("Enter Website URL")

if st.button("Index Website"):
    if not url:
        st.error("Please enter a URL.")
        st.stop()

    if not validate_url(url):
        st.error("Invalid or unreachable URL.")
        st.stop()

    with st.spinner("Crawling and indexing website..."):
        docs = crawl_and_clean(url)

        if not docs:
            st.error("No meaningful content found on this website.")
            st.stop()

        st.session_state.vectorstore = create_vectorstore(docs)
        st.success("Website indexed successfully!")

# ---------- CHAT ----------
if "vectorstore" in st.session_state:
    qa_chain = build_qa_chain(st.session_state.vectorstore)

    user_q = st.chat_input("Ask a question about the website")

    if user_q:
        result = qa_chain.invoke(
            {"question": user_q},
            config={"configurable": {"session_id": "default"}}
        )
        st.write(result.content)
