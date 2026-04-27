# 🦜🔗 Ask the Doc - LangChain Streamlit Application

**Week 15 Lab Assignment | Programming for Data Analytics / AI Applications / Web Development**

An AI-powered Streamlit web application that answers questions about uploaded text documents using LangChain, OpenAI embeddings, and the Chroma vector database.

## ✨ Features

- 📄 Upload text documents (.txt files)
- 🤖 Ask questions about your documents
- 🧠 Powered by OpenAI GPT-3.5-turbo
- 📊 Uses semantic search with vector embeddings
- 🚀 Deploy in minutes to Streamlit Cloud

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- OpenAI API key ([get one here](https://platform.openai.com/api-keys))

### Installation

```bash
# Clone or download this repository
# Then:

# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py

# 3. Open your browser
# The app will open at http://localhost:8501
```

## 📖 How to Use

1. **Upload a Document** - Click "Upload a text document" and select a .txt file
2. **Ask a Question** - Type your question about the document
3. **Provide API Key** - Enter your OpenAI API key (not stored)
4. **Click Submit** - Wait for the AI to generate an answer

## 📁 Files Included

| File | Purpose |
|------|---------|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Python dependencies |
| `SETUP_GUIDE.md` | Detailed setup instructions |
| `ASSIGNMENT_SUMMARY.md` | Assignment overview and concepts |
| `sample_document.txt` | Sample document for testing |
| `README.md` | This file |

## 🔧 How It Works

```
Document Upload
    ↓
Split into Chunks (CharacterTextSplitter)
    ↓
Convert to Embeddings (OpenAIEmbeddings)
    ↓
Store in Vector DB (Chroma)
    ↓
User Question
    ↓
Retrieve Relevant Chunks
    ↓
Pass to LLM (OpenAI)
    ↓
Return Answer
```

## 💡 Key Concepts

### Embeddings
Text is converted into numerical vectors that capture semantic meaning. Similar text produces similar vectors.

### Vector Store
Chroma stores embedding vectors and enables fast semantic search to find relevant document chunks.

### Retrieval QA Chain
LangChain component that retrieves relevant document chunks and passes them with your question to the LLM for context-aware answers.

## 🧪 Testing

Use the included `sample_document.txt` file to test the app:

**Example Questions:**
- "What did the document mention about LLMs?"
- "What were the key initiatives discussed?"
- "What did the document say about Ketanji Brown Jackson?"

## 📚 Documentation

For detailed setup, deployment, and troubleshooting:
- Read **SETUP_GUIDE.md** for installation and deployment
- Read **ASSIGNMENT_SUMMARY.md** for concepts and requirements

## 🚢 Deployment

### Deploy to Streamlit Cloud

1. Push your files to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New app" and select your repo
4. Add your OpenAI API key in Secrets
5. Deploy!

See SETUP_GUIDE.md for detailed instructions.

## ⚙️ Customization

### Change Chunk Size
In `app.py`, line 37:
```python
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
# Increase chunk_size for larger context windows
```

### Support More File Types
```python
# Add to requirements: pip install PyPDF2 python-docx

# Then handle multiple formats:
uploaded_file = st.file_uploader('Upload a document', type=['txt', 'pdf', 'docx'])
```

### Use Different LLMs
```python
from langchain.llms import HuggingFaceLLM
# Replace OpenAI with other LLM providers
```

## ⚠️ Security Notes

- **Never commit your API key** to version control
- **Don't hardcode keys** in your application
- Use environment variables or Streamlit secrets
- The app doesn't store or log API keys
- Revoke compromised keys immediately in your OpenAI dashboard

## 🐛 Troubleshooting

**"ModuleNotFoundError"**
```bash
pip install -r requirements.txt
```

**"Invalid API Key"**
- Check your key is correct
- Verify your OpenAI account has active billing
- Generate a new key if needed

**"Slow Performance"**
- Reduce chunk_size
- Use smaller test documents
- Check OpenAI API status

See SETUP_GUIDE.md for more troubleshooting.

## 📖 Learning Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenAI API Guide](https://platform.openai.com/docs/guides/embeddings)
- [RAG Pattern Explained](https://python.langchain.com/docs/use_cases/question_answering/)

## 📊 Technical Stack

| Component | Version | Purpose |
|-----------|---------|---------|
| Streamlit | 1.28.1 | Web framework |
| LangChain | 0.0.340 | LLM orchestration |
| OpenAI | 1.3.7 | LLM API |
| Chroma | 0.4.14 | Vector database |
| Tiktoken | 0.5.1 | Tokenizer |

## 📝 Assignment Info

- **Course:** Programming for Data Analytics / AI Applications / Web Development
- **Week:** 15
- **Points:** 10
- **Topic:** Document Question-Answering with LangChain

## ✅ Grading Checklist

- [ ] Code runs without errors
- [ ] Proper file uploads work
- [ ] Questions are answered with relevant context
- [ ] API key handling is secure
- [ ] Setup instructions are clear
- [ ] All files are included

## 🤝 Contributing

This is an assignment. For your own enhancements:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

## 📄 License

Educational use only - Week 15 Lab Assignment

## 👤 Author

Your Name | Programming for Data Analytics Student

---

**Need help?** See SETUP_GUIDE.md or ASSIGNMENT_SUMMARY.md

**Ready to deploy?** Check the Deployment section above

**Want to learn more?** Check the Resources section

Happy coding! 🚀🦜🔗
