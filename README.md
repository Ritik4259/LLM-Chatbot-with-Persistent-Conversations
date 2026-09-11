# LLM Chatbot with Persistent Conversations

An end-to-end conversational AI application built using **LangChain**, **LangGraph**, **Streamlit**, and **SQLite**. This repository features multi-threaded persistent chat history, real-time response streaming, modular backend architecture, and **LangSmith** integration for observability and monitoring.

---

## Features

* **Persistent Multi-Threaded Conversations**: Stateful chat execution managed using LangGraph's SQLite checkpointer (`SqliteSaver`), allowing seamless thread creation, retrieval, and conversation history resumption across sessions.
* **Real-time Streaming**: Response generation streamed token-by-token directly to the Streamlit UI using LangChain stream handlers.
* **Modular Architecture**: Separate modules for graph execution, SQLite storage management, streaming components, and frontend application logic.
* **LangSmith Observability**: Built-in integration for tracking model calls, execution traces, latency, and token consumption.
* **Streamlit UI**: Clean, intuitive Web UI with dynamic thread switching and real-time chat updates.

---

## Repository Structure

```text
├── chatbot_database_backend.py   # Database integration & checkpointer management
├── chatbot_database_frontend.py  # Frontend interactions for database state/threads
├── chatbot_langgraph_backend.py # LangGraph graph definitions and state nodes
├── chatbot_streaming.py         # Custom streaming handlers for real-time output
├── chatbot_threading.py         # Thread management and state persistence execution
├── chatbotui.py                 # Streamlit UI application entry point
└── README.md                    # Project documentation

```

---

## Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ritik4259/LLM-Chatbot-with-Persistent-Conversations.git
cd LLM-Chatbot-with-Persistent-Conversations

```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install langchain langgraph langchain-openai streamlit sqlite3 langsmith

```

*(Adjust requirements based on your specific LLM provider, e.g., `langchain-anthropic`, `langchain-google-genai`).*

---

## Environment Configuration

Create a `.env` file in the root directory and add your API keys:

```ini
# OpenAI / Primary LLM API Key
OPENAI_API_KEY=your_openai_api_key_here

# LangSmith Observability Configuration (Optional)
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=llm-chatbot-persistent

```

---

## How to Run

Launch the Streamlit interface using:

```bash
streamlit run chatbotui.py

```

Open your browser at `http://localhost:8501` to start interacting with the chatbot.

---

## Key Workflow

1. **Session Setup**: Select or create a thread ID in the sidebar.
2. **State Checkpointing**: User inputs are sent to the LangGraph backend, where state is preserved in `SQLite`.
3. **Streamed Generation**: The response streams back to the Streamlit frontend in real time.
4. **History Retrieval**: Previous conversations can be reloaded at any time via the stored thread checkpointer.

## Futher upcoming upgrades

1. RAG implementation
2. MCP connection
3. Deployment
