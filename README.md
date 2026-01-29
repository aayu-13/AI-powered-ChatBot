# AI-Powered Website Chatbot (RAG-based)
📌 Project Overview

This project implements an AI-powered chatbot that allows users to ask questions strictly based on the content of a provided website URL.The system crawls and extracts meaningful textual content from the website, converts it into embeddings, stores them in a vector database, and uses a Large Language Model (LLM) to generate context-aware, grounded answers.

⚠️ The chatbot does not use external knowledge.
        If the answer is not present on the website, it responds exactly with:
        “The answer is not available on the provided website.”

🧠 System Architecture
        High-Level Flow
        User (Streamlit UI)
                ↓
        Website URL Input
                ↓
        Website Crawler & Cleaner
                ↓
        Text Chunking
                ↓
        Embedding Generation
                ↓
        Vector Database (ChromaDB)
                ↓
        Retriever
                ↓
        LLM (Gemini 1.5 Flash)
                ↓
        Answer (Strictly from Website Content)

🧩 Components Explained
1. User Interface (Streamlit)

   * Built using Streamlit
   * Allows users to:
     * Enter a website URL
     * Index website content
     * Ask questions via a chat interface
     * View chatbot responses clearly

2. Website Crawling & Content Extraction

   * Uses WebBaseLoader to fetch HTML pages
   * Uses BeautifulSoup to:
     * Remove headers, footers, navigation menus, scripts, styles, ads
     * Extract only meaningful textual content
   * Handles:
     * Invalid URLs
     * Unreachable websites
     * Empty or unsupported content gracefully

3. Text Processing & Chunking

   * Cleaned text is split using RecursiveCharacterTextSplitter
   * Configurable parameters:
     * chunk_size = 1000
     * chunk_overlap = 150
   * Each chunk maintains metadata such as:
     * Source URL
     * Page content reference

4. Embedding Strategy

   * Embedding Model Used:
     sentence-transformers/all-MiniLM-L6-v2

   Why this embedding model?
   * Free and open-source
   * Runs locally (no API quota issues)
   * Fast and memory-efficient
   * Widely used in Retrieval-Augmented Generation (RAG) systems

5. Vector Database

   * Vector Store Used: ChromaDB

   Why ChromaDB?
        
   * Lightweight and easy to use
   * Supports persistent storage
   * Suitable for small-to-medium scale projects
   * Ideal for local development and academic assignments
   * Embeddings are persisted on disk and reused across sessions.

6. LLM Model

   * LLM Used: Gemini 1.5 Flash
   Why Gemini 1.5 Flash?
   * Fast inference speed
   * Strong reasoning and summarization
   * Cost-efficient
   * Well-suited for conversational QA

7. Question Answering Logic

   * Uses LangChain LCEL (Runnable architecture)
   * Retrieval step fetches only relevant chunks
   * Prompt design ensures:
     * Answers are generated only from retrieved context
     * No hallucination or external knowledge
        
   If no relevant context is found, the chatbot responds exactly:
      “The answer is not available on the provided website.”

9. Conversational Memory

   * Implements short-term session memory
   * Uses StreamlitChatMessageHistory
   * Maintains context across multiple user queries
   * Memory is limited to the current session only

⚙️ Frameworks & Libraries Used
        | Category      | Tool                          |
| ------------- | ----------------------------- |
| UI            | Streamlit                     |
| LLM           | Gemini 1.5 Flash              |
| Embeddings    | SentenceTransformers (MiniLM) |
| Vector DB     | ChromaDB                      |
| Orchestration | LangChain (LCEL)              |
| Web Scraping  | BeautifulSoup                 |
| Language      | Python                        |

▶️ Setup & Run Instructions
1. Clone the Repository
   ```
   git clone <your-github-repo-url>
   cd <project-folder>

2. Create Virtual Environment
   ```
   python -m venv myenv
   source myenv/bin/activate  # Windows: myenv\Scripts\activate

3. Install Dependencies
   ```
   pip install -r requirements.txt

4. Run the Application
   ```
   streamlit run app.py

5. Enter Google API Key
   * Enter your Gemini API key in the sidebar
   * Paste a valid website URL
   * Click Index Website
   * Start asking questions

🔒 Security Considerations

   * No API keys are hardcoded
   * API keys are provided via user input
   * Sensitive data is not logged or stored

⚠️ Assumptions & Limitations

   * Only HTML-based websites are supported
   * JavaScript-heavy sites may have limited extraction
   * The chatbot cannot answer questions outside website content
   * Large websites may take longer to index

🚀 Future Improvements

   * Multi-page crawling and sitemap support
   * Source citations for answers
   * Multi-URL ingestion
   * User authentication
   * Deployment on Streamlit Cloud or HuggingFace Spaces

📎 Conclusion

   This project demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline with strong emphasis on grounded responses, clean architecture, and real-world constraints such as rate limits and persistence.
