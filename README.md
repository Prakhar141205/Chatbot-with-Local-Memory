# Chatbot with Memory

A small Streamlit chatbot that includes the current conversation in each request, allowing the model to refer back to earlier messages in the same session. It supports OpenAI, Google Gemini, and a locally running Ollama model.

## Requirements

- Python 3.10 or newer
- An API key for OpenAI or Gemini, or a running Ollama server with a model downloaded

## Setup

1. Clone or download this project and open a terminal in its directory.
2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows PowerShell, activate it with:

   ```powershell
   .venv\Scripts\Activate.ps1
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and configure a provider. For example, to use Gemini:

   ```dotenv
   LLM_PROVIDER=gemini
   GEMINI_API_KEY=your-gemini-api-key
   GEMINI_MODEL=gemini-2.0-flash
   ```

   Do not commit your `.env` file or share your API keys.

## Choose a provider

Set `LLM_PROVIDER` in `.env` to one of the supported values:

| Provider | Required settings | Defaults |
| --- | --- | --- |
| `gemini` | `GEMINI_API_KEY` | Model: `gemini-2.0-flash` |
| `openai` | `OPENAI_API_KEY` | Model: `gpt-4o-mini` |
| `ollama` | Ollama running locally with the selected model available | URL: `http://localhost:11434`; model: `llama3.2` |

For Ollama, start the Ollama server and download the default model if needed:

```bash
ollama pull llama3.2
```

You can override the model and Ollama URL with `OLLAMA_MODEL` and `OLLAMA_BASE_URL`. Set a different model with `GEMINI_MODEL` or `OPENAI_MODEL` for those providers.

The assistant's system prompt can be changed with `SYSTEM_PROMPT`. If omitted, the app uses a friendly, concise default prompt.

## Run

Start the Streamlit app from the project directory:

```bash
streamlit run app.py
```

Streamlit opens the app in your browser. Enter a message in the chat box to begin. Use **Clear conversation** to start a fresh conversation.

## Conversation memory

The app sends the system prompt, the conversation history, and the latest message to the selected model for each response. This lets the model use earlier messages as context. History is kept in Streamlit session state for the current browser session; it is not saved to a database and may be lost when the session ends.

## Project files

- `app.py` — Streamlit user interface and session-based chat history
- `config.py` — provider selection, environment variables, and configuration checks
- `llm_client.py` — API clients for OpenAI, Gemini, and Ollama
- `memory.py` — in-memory conversation history helper
- `chatbot_with_memory.py` — separate command-line prototype
- `requirements.txt` — Python dependencies


## Note: 
- The user interface of this mini-project was developed with the assistance of AI tools using Streamlit.
