from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_community.chat_message_histories import StreamlitChatMessageHistory

def build_qa_chain(vectorstore):
    """Build retrieval-augmented QA chain with memory."""

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Answer ONLY using the provided context. "
            "If the answer is not present, respond exactly with:\n"
            "“The answer is not available on the provided website.”"
        ),
        ("human", "Context:\n{context}\n\nQuestion:\n{question}")
    ])

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0
    )

    retriever = vectorstore.as_retriever()

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {
            "context": retriever | format_docs,
            "question": lambda x: x["question"]
        }
        | prompt
        | llm
    )

    history = StreamlitChatMessageHistory(key="chat_history")

    return RunnableWithMessageHistory(
        chain,
        lambda session_id: history,
        input_messages_key="question",
        history_messages_key="history"
    )
