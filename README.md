# 🕉️ GITA-GPT - Divine Wisdom Explorer

<img width="1560" height="865" alt="GITA-GPT Screenshot" src="https://github.com/user-attachments/assets/a99aafc1-8820-4ed5-b63a-788e279d2938" />

**DEMO**: https://youtu.be/_aAi9S8k2yE

A modern AI-powered Q&A system for the Bhagavad Gita, using Retrieval-Augmented Generation (RAG) with ChromaDB, FastAPI, and a beautiful custom frontend. Ask any question about the sacred teachings and receive contextually accurate answers backed by relevant verses.

---

## ✨ Features

- 🤖 **Intelligent Q&A**: Ask any question about the Bhagavad Gita and get context-aware answers
- 🔍 **Semantic Search**: Advanced vector-based search over verses using sentence transformers
- ⚡ **FastAPI Backend**: High-performance API with Groq LLM integration
- 🌐 **ChromaDB Integration**: Support for both Cloud and local vector databases
- 🎨 **Modern Frontend**: Beautiful, responsive web interface with smooth UX
- 📚 **Comprehensive Data**: Complete Bhagavad Gita dataset with verse mappings
- 🔒 **Environment Security**: Secure API key management with dotenv

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   FastAPI       │    │   Vector DB     │
│   (HTML/CSS/JS) │◄──►│   Backend       │◄──►│   (ChromaDB)    │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Groq LLM      │
                       │   Integration   │
                       └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Groq API key ([Get one here](https://console.groq.com/))
- ChromaDB credentials (optional, for cloud deployment)

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Gita-GPT
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv myenv
   myenv\Scripts\activate  # Windows
   # source myenv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   
   # Optional: ChromaDB Cloud (if using cloud deployment)
   CHROMA_TENANT=your_tenant
   CHROMA_DATABASE=your_database
   CHROMA_API_KEY=your_chroma_api_key
   ```

5. **Initialize the vector database**
   ```bash
   python create_chroma_index.py
   ```

6. **Start the API server**
   ```bash
   python api.py
   ```

7. **Access the application**
   Open your browser and navigate to `http://localhost:8000`

## 📁 Project Structure

```
Gita-GPT/
├── api.py                    # FastAPI backend server
├── base.py                   # Base configuration and utilities
├── create_chroma_index.py    # Vector database initialization
├── gita_data.json           # Bhagavad Gita dataset
├── gita.csv                 # Alternative CSV format
├── requirements.txt         # Python dependencies
├── README.md               # Project documentation
├── static/                 # Frontend assets
│   ├── index.html         # Main web interface
│   ├── styles.css         # Styling
│   └── script.js          # Frontend JavaScript
└── myenv/                 # Virtual environment (auto-created)
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GROQ_API_KEY` | Your Groq API key for LLM integration | Yes |
| `CHROMA_TENANT` | ChromaDB Cloud tenant (if using cloud) | No |
| `CHROMA_DATABASE` | ChromaDB database name | No |
| `CHROMA_API_KEY` | ChromaDB Cloud API key | No |

### Local vs Cloud Deployment

The application supports both local ChromaDB and ChromaDB Cloud:
- **Local**: Automatically falls back to local storage if cloud credentials aren't provided
- **Cloud**: Set the ChromaDB environment variables for scalable cloud deployment

## 🛠️ API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve the main web interface |
| `/search` | POST | Search for relevant verses |
| `/ask` | POST | Ask questions and get AI responses |
| `/health` | GET | Health check endpoint |

### Example API Usage

```python
import requests

# Ask a question
response = requests.post("http://localhost:8000/ask", 
    json={"question": "What does Krishna say about dharma?"})
print(response.json())
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Bhagavad Gita teachings and wisdom
- ChromaDB for vector database capabilities
- Groq for fast LLM inference
- FastAPI for the robust backend framework
- Sentence Transformers for semantic embeddings

---

**Made with ❤️ for seekers of divine wisdom**src="https://github.com/user-attachments/assets/a99aafc1-8820-4ed5-b63a-788e279d2938" />

# GITA-GPT

A modern AI-powered Q&A system for the Bhagavad Gita, using Retrieval-Augmented Generation (RAG) with ChromaDB Cloud, FastAPI, and a beautiful custom frontend.

---

## Features
- **Ask any question** about the Bhagavad Gita and get context-aware answers
- **Semantic search** over verses using vector embeddings
- **FastAPI backend** with Groq LLM integration
- **ChromaDB Cloud** for scalable, managed vector search
- **Modern frontend** (HTML/CSS/JS) with smooth UX


To run the code simply do:

```bash
#0 Get a GROQ API key and store it as GROQ_API_KEY

# 1. Install dependencies
pip install -r requirements.txt

# 2. Start the API server
python api.py
