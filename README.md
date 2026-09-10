# Simple RAG Chatbot with Langchain

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)

## 📋 Overview

A domain-specific chatbot application that combines the power of **Large Language Models (LLMs)** with the efficiency of **vector databases** to provide accurate, context-aware responses. This project implements the **Retrieval-Augmented Generation (RAG)** method for enhanced question-answering capabilities.

## ✨ Key Features

- 🤖 **RAG-based Architecture**: Combines document retrieval with LLM generation for accurate answers
- 🚀 **Multiple LLM Support**: Hugging Face models and Gemma via Ollama
- 🗄️ **Vector Database Integration**: Pinecone for efficient similarity search
- 🎨 **User-Friendly Interface**: Built with Streamlit for easy interaction
- 📚 **Document-Based Learning**: Feed custom documents for domain-specific responses
- ⚡ **Fast & Efficient**: Optimized retrieval and response generation

## 🛠️ Technology Stack

| Component | Technology |
|-----------|----------|
| **Frontend** | Streamlit |
| **Vector Database** | Pinecone / FAISS |
| **LLM Framework** | LangChain |
| **Language Models** | Hugging Face, Gemma (via Ollama) |
| **Backend** | Python 3.12 |

## 📂 Project Structure

```
Simple-RAG-Chatbot/
├── src/
│   ├── chatbot.py              # Core chatbot logic
│   ├── streamlitMain.py        # Streamlit UI
│   └── materials/              # Document data for RAG
├── report/                     # Generated reports
├── .env                        # API keys (create locally)
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔧 Installation

### Prerequisites
- Python 3.12+
- pip package manager
- Git

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rahul19873/Simple-RAG-Chatbot.git
   cd Simple-RAG-Chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env` (if available) or create a new `.env` file
   - Add your API keys:
     ```
     HUGGINGFACE_API_KEY=your_key_here
     PINECONE_API_KEY=your_key_here
     PINECONE_INDEX_NAME=your_index
     ```

5. **Set up your LLM**
   - For Ollama: [Install Ollama](https://ollama.ai/) and pull the Gemma model
     ```bash
     ollama pull gemma
     ```
   - For Hugging Face: Ensure your API key is set in `.env`

6. **Run the application**
   ```bash
   cd src
   streamlit run streamlitMain.py
   ```

7. **Access the chatbot**
   - Open your browser and navigate to: `http://localhost:8501`

## 📖 Usage

### Quick Start

1. Start the Streamlit application (see Installation step 6)
2. Upload or configure your document source in the sidebar
3. Ask questions about your documents
4. Receive AI-generated answers based on retrieved context

### Example Queries

```
"What are the main topics covered in the documents?"
"Explain [specific concept] from the materials"
"Summarize the key findings"
```

## 🔌 Configuration

### Vector Database Setup
**FAISS (Local Alternative):**
- No external API required
- Better for privacy-sensitive applications
- Requires local storage

### LLM Selection

Update `chatbot.py` to select your preferred model:
```python
# Option 1: Ollama (Local)
llm = OllamaLLM(model="gemma")

# Option 2: Hugging Face
llm = HuggingFaceLLM(model_name="model-name", api_key=os.getenv("HUGGINGFACE_API_KEY"))
```

## 📦 Dependencies

Core dependencies listed in `requirements.txt`:
- `langchain` - RAG framework
- `streamlit` - Frontend interface
- `faiss-cpu` or `faiss-gpu` - Local vector search
- `python-dotenv` - Environment variable management
- `huggingface-hub` - Hugging Face integration

For a complete list, see `requirements.txt`

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'X'"
**Solution:** Reinstall dependencies
```bash
pip install -r requirements.txt --upgrade
```

### Issue: "API key not found"
**Solution:** Verify your `.env` file contains all required keys:
```bash
cat .env  # Check contents (don't commit this file!)
```

### Issue: Pinecone connection error
**Solution:** Check your network connection and API credentials

### Issue: LLM model not responding
**Solution:** 
- If using Ollama: Ensure `ollama serve` is running
- If using Hugging Face: Verify API key and rate limits

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- How to submit issues
- How to create pull requests
- Code standards and best practices
- Development setup

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [LangChain](https://langchain.com/) - RAG framework
- [Streamlit](https://streamlit.io/) - Interactive UI library
- [Pinecone](https://www.pinecone.io/) - Vector database
- [Ollama](https://ollama.ai/) - Local LLM support

## 📞 Support

- 💬 Open an [Issue](https://github.com/Rahul19873/Simple-RAG-Chatbot/issues) for bug reports
- 💡 Start a [Discussion](https://github.com/Rahul19873/Simple-RAG-Chatbot/discussions) for questions
- 🔄 Submit a [Pull Request](https://github.com/Rahul19873/Simple-RAG-Chatbot/pulls) with improvements

---

**Made with ❤️ by [Rahul19873](https://github.com/Rahul19873)**
