# Ask the Doc Application - Setup Guide

## Week 15 LangChain Lab Assignment

This guide walks you through setting up and running the "Ask the Doc" Streamlit application locally or deploying it to Streamlit Cloud.

---

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Local Setup](#local-setup)
3. [Get OpenAI API Key](#get-openai-api-key)
4. [Running Locally](#running-locally)
5. [Deploying to Streamlit Cloud](#deploying-to-streamlit-cloud)
6. [Testing the App](#testing-the-app)
7. [Troubleshooting](#troubleshooting)

---

## Prerequisites

- **Python**: Version 3.7 or higher
- **pip**: Python package manager
- **OpenAI Account**: For API access
- **Git** (optional): For deploying to Streamlit Cloud

### Check Python Version
```bash
python --version
# or
python3 --version
```

---

## Local Setup

### Step 1: Clone or Download the Project Files

Place these files in your project directory:
- `app.py` - Main Streamlit application
- `requirements.txt` - Python dependencies

### Step 2: Create a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

**What gets installed:**
- `streamlit` - Web app framework
- `langchain` - LLM orchestration library
- `openai` - OpenAI API client
- `chromadb` - Vector database for embeddings
- `tiktoken` - Tokenizer for OpenAI models

---

## Get OpenAI API Key

### Step 1: Create OpenAI Account
1. Go to [https://platform.openai.com/](https://platform.openai.com/)
2. Sign up or log in to your account

### Step 2: Generate API Key
1. Click on your profile icon (top right)
2. Select "API keys" or go to [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
3. Click "Create new secret key"
4. Copy the key immediately (you won't see it again!)
5. Store it safely

### Step 3: Add Billing (If Needed)
- Set up billing in your OpenAI account to use the API
- Check pricing: [https://openai.com/pricing](https://openai.com/pricing)
- You get $5 free credit initially

### ⚠️ Important Security Notes
- **Never commit your API key** to version control
- **Don't share your API key** with others
- Use environment variables (optional) for local development:
  ```bash
  # Create a .env file (add to .gitignore)
  OPENAI_API_KEY=your_key_here
  ```

---

## Running Locally

### Step 1: Navigate to Project Directory
```bash
cd path/to/your/project
```

### Step 2: Activate Virtual Environment
```bash
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Run the App
```bash
streamlit run app.py
```

### Step 4: Access the App
- The app will open in your default browser at `http://localhost:8501`
- If it doesn't open, manually go to that URL

---

## Deploying to Streamlit Cloud

### Step 1: Prepare Your Repository

1. Create a GitHub repository for your project
2. Push these files:
   - `app.py`
   - `requirements.txt`
   - `README.md` (optional)

### Step 2: Deploy on Streamlit Cloud

1. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Click "New app"
3. Select:
   - Your GitHub repository
   - Branch: `main`
   - File: `app.py`
4. Click "Deploy!"

### Step 3: Add Secrets (Important!)

In Streamlit Cloud dashboard:
1. Click the settings icon (gear icon, top right)
2. Go to "Secrets"
3. Add your OpenAI API key (not required if users provide it in the app)

**secrets.toml example:**
```toml
OPENAI_API_KEY = "sk-..."
```

---

## Testing the App

### Test File: state_of_the_union.txt

Use this sample text to test:

```
In recent months, large language models (LLMs) have attracted widespread attention as they open up new opportunities for developers creating chatbots, personal assistants, and content. In previous tutorials, you learned about three key LangChain modules: model I/O, data connection, and chains.

The State of the Union address highlighted several key points about the economy, infrastructure, and future technology initiatives. The president emphasized the importance of investing in artificial intelligence and supporting workers transitioning to new technology roles.

Key achievements this year include passage of the Infrastructure Act, investment in clean energy, and support for manufacturing jobs in critical sectors like semiconductors.
```

### Test Questions
1. "What did the document mention about LLMs?"
2. "What were the key topics discussed?"
3. "What did the president say about investing in AI?"

### Expected Output
The app should return relevant answers extracted from the document using the LLM.

---

## How the App Works

### High-Level Flow

```
User Input
    ↓
Upload Document → Split into Chunks → Create Embeddings
    ↓
Store in Vector Database (Chroma)
    ↓
User Question
    ↓
Search Vector DB for Relevant Chunks → Feed to LLM
    ↓
LLM Generates Answer
    ↓
Display Result
```

### Key Components

| Component | Purpose |
|-----------|---------|
| **CharacterTextSplitter** | Splits documents into manageable chunks (1000 chars, 0 overlap) |
| **OpenAIEmbeddings** | Converts text chunks into numerical vectors (embeddings) |
| **Chroma** | Vector database that stores and retrieves similar chunks |
| **RetrievalQA** | Chain that retrieves relevant chunks and passes to LLM |
| **OpenAI LLM** | Generates natural language answers |

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"

**Solution:**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Then install again
pip install -r requirements.txt
```

### Issue: "Invalid API Key"

**Solution:**
- Verify your API key is correct
- Check that your OpenAI account has active billing
- Ensure key hasn't been revoked in your OpenAI dashboard

### Issue: "ConnectionError" or "Timeout"

**Solution:**
- Check your internet connection
- OpenAI API might be temporarily down (check status.openai.com)
- Try again after a few moments

### Issue: "embeddingModel not found" or Chroma errors

**Solution:**
```bash
pip install --upgrade chromadb
pip install --upgrade langchain
```

### Issue: App is slow or hangs

**Solution:**
- Reduce chunk size in app.py (currently 1000)
- Use a smaller document for testing
- Check OpenAI API rate limits

---

## Code Explanation

### Main Function: `generate_response()`

```python
def generate_response(uploaded_file, openai_api_key, query_text):
    # 1. Load the document
    document = uploaded_file.read().decode('utf-8')
    
    # 2. Split into chunks for better retrieval
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_text(document)
    
    # 3. Create embeddings (numerical representations)
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    
    # 4. Store in vector database
    db = Chroma.from_texts(texts, embeddings)
    
    # 5. Create retriever for searching
    retriever = db.as_retriever()
    
    # 6. Create QA chain
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=openai_api_key),
        chain_type='stuff',
        retriever=retriever
    )
    
    # 7. Run the chain and return answer
    response = qa.run(query_text)
    return response
```

---

## Key LangChain Concepts

### Embeddings
- Convert text to numerical vectors
- Similar text = similar vectors
- Enables semantic search

### Vector Store (Chroma)
- Stores embedding vectors
- Enables fast similarity search
- Returns most relevant chunks for a query

### Retrieval QA Chain
- Retrieves relevant document chunks
- Passes them to LLM with the question
- LLM generates answer based on context

### Chain Type: 'stuff'
- Concatenates all retrieved documents
- Passes them as context to the LLM
- Simple but effective for smaller documents

---

## Assignment Requirements Checklist

- [ ] Create app.py with all LangChain components
- [ ] Create requirements.txt with dependencies
- [ ] Test app locally with sample document
- [ ] Verify app works with different questions
- [ ] Deploy to Streamlit Cloud (or submit local files)
- [ ] Document any modifications or enhancements

---

## Next Steps

1. **Enhance the App:**
   - Add support for different file types (PDF, DOCX)
   - Implement conversation history
   - Add document metadata display

2. **Optimize Performance:**
   - Experiment with different chunk sizes
   - Try different embedding models
   - Implement caching

3. **Deploy:**
   - Push to GitHub
   - Deploy to Streamlit Cloud
   - Share with others!

---

## Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Reference](https://platform.openai.com/docs/api-reference)
- [Chroma Documentation](https://docs.trychroma.com/)

---

**Assignment Worth: 10 points**  
**Course: Programming for Data Analytics / AI Applications / Web Application Development**  
**Week: 15**

Good luck! 🦜🔗
