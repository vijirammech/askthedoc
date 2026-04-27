# Week 15 LangChain Lab 4: Ask the Doc App - Complete Summary

## Assignment Overview

**Title:** Build an Ask the Doc App  
**Week:** 15  
**Points:** 10  
**Applicable To:** 
- AI Applications Students
- Web Application Development Students  
- Programming for Data Analytics Students

**Objective:** Create a Streamlit web application that uses LangChain, OpenAI embeddings, and a vector store to answer questions about uploaded text documents.

---

## What You're Building

An interactive web application (`Ask the Doc`) that enables users to:
1. **Upload a text document** (.txt file)
2. **Ask questions** about the document
3. **Receive AI-powered answers** based on the document content

### Example Use Case
- Upload: "State of the Union address"
- Question: "What did the president say about infrastructure?"
- Answer: "The president emphasized the importance of..."

---

## Core Concepts Covered

### 1. **Document Embeddings**
- Text is converted to numerical vectors (embeddings)
- Similar content = similar vectors
- Used for semantic search

### 2. **Vector Store (Chroma)**
- Database that stores embedding vectors
- Enables fast retrieval of relevant document chunks
- Returns most similar chunks to user's question

### 3. **Text Chunking**
- Documents split into manageable pieces (1000 characters)
- Each chunk gets its own embedding
- Improves retrieval accuracy

### 4. **Retrieval QA Chain**
- Searches vector store for relevant chunks
- Passes chunks + question to LLM
- LLM generates answer based on context

### 5. **Streamlit Framework**
- Web framework for building data apps
- No frontend expertise needed
- Simple Python-based UI components

---

## Technical Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  STREAMLIT WEB APP                      │
├─────────────────────────────────────────────────────────┤
│  User Interface:                                        │
│  • File Upload (*.txt)                                  │
│  • Question Input                                       │
│  • API Key Input                                        │
│  • Submit Button                                        │
└──────────┬──────────────────────────────────────────────┘
           │
           ↓ generate_response()
┌─────────────────────────────────────────────────────────┐
│                LANGCHAIN PIPELINE                       │
├─────────────────────────────────────────────────────────┤
│  1. Load Document                                       │
│  2. CharacterTextSplitter → Break into chunks          │
│  3. OpenAIEmbeddings → Convert to vectors              │
│  4. Chroma → Store embeddings                          │
│  5. Retriever → Find relevant chunks                   │
│  6. RetrievalQA → Combine with LLM                     │
│  7. OpenAI LLM → Generate answer                       │
└──────────┬──────────────────────────────────────────────┘
           │
           ↓
┌─────────────────────────────────────────────────────────┐
│                   RESPONSE                              │
│  "The answer to your question is..."                   │
└─────────────────────────────────────────────────────────┘
```

---

## Deliverables

### Files Provided

1. **app.py** (98 lines)
   - Complete Streamlit application
   - `generate_response()` function with 6 key steps
   - Web UI with file upload, question input, API key field
   - Error handling and user feedback

2. **requirements.txt**
   - All Python dependencies with pinned versions
   - Ensures reproducibility across machines

3. **SETUP_GUIDE.md**
   - Step-by-step installation instructions
   - How to get OpenAI API key
   - Local testing instructions
   - Deployment guide to Streamlit Cloud
   - Troubleshooting common issues

4. **ASSIGNMENT_SUMMARY.md** (this file)
   - Overview of concepts and requirements
   - Architecture explanation
   - Code breakdown

---

## Key Code Components

### Step 1: Load Document
```python
document = uploaded_file.read().decode('utf-8')
```
Reads the uploaded text file as a string.

### Step 2: Split into Chunks
```python
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_text(document)
```
Breaks document into 1000-character chunks for better retrieval.

### Step 3: Create Embeddings
```python
embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
```
Initializes the embedding model (converts text to vectors).

### Step 4: Store in Vector Database
```python
db = Chroma.from_texts(texts, embeddings)
```
Stores all text chunks and their embeddings in Chroma.

### Step 5: Create Retriever
```python
retriever = db.as_retriever()
```
Creates interface to search the vector store.

### Step 6: Build QA Chain
```python
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(openai_api_key=openai_api_key),
    chain_type='stuff',
    retriever=retriever
)
```
Combines retriever with LLM for question answering.

### Step 7: Run and Return Answer
```python
response = qa.run(query_text)
return response
```
Executes the chain and returns the LLM's answer.

---

## Dependencies Explained

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | 1.28.1 | Web framework for the UI |
| langchain | 0.0.340 | LLM orchestration and chains |
| openai | 1.3.7 | OpenAI API client |
| chromadb | 0.4.14 | Vector database for embeddings |
| tiktoken | 0.5.1 | Tokenizer (counts text tokens) |
| python-dotenv | 1.0.0 | Load environment variables |

---

## How to Run

### Quick Start (3 steps)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the app
streamlit run app.py

# 3. Use the app
# - Upload a .txt file
# - Ask a question
# - Provide your OpenAI API key
# - Click Submit
```

### Input Requirements
- **File:** Text file (.txt format)
- **Question:** Any question about the document content
- **API Key:** Valid OpenAI API key with active billing

### What You Get
- Natural language answer extracted from your document
- Powered by GPT-3.5-turbo or similar LLM
- Based on semantic search and document context

---

## Grading Rubric (10 points)

| Criterion | Points | Description |
|-----------|--------|-------------|
| **Code Quality** | 3 | Clean, documented code following PEP8 |
| **Functionality** | 3 | App runs without errors, all features work |
| **LangChain Implementation** | 2 | Correct use of embeddings, vector store, chain |
| **Deployment/Submission** | 2 | Proper setup instructions and file organization |

---

## Common Questions & Answers

### Q: What if my API key is exposed?
**A:** Immediately revoke it in your OpenAI dashboard and generate a new one.

### Q: Can I use other LLMs besides OpenAI?
**A:** Yes! LangChain supports Hugging Face, Cohere, Anthropic, etc. Modify the LLM initialization.

### Q: What document formats are supported?
**A:** Currently .txt only. For PDF/DOCX, use PyPDF2 or python-docx to extract text first.

### Q: How much does the OpenAI API cost?
**A:** Depends on tokens used. GPT-3.5-turbo is ~$0.0005 per 1K tokens. Budget: $1-5 for testing.

### Q: Can I make this production-ready?
**A:** Yes! Add:
- User authentication
- Document persistence
- Multi-turn conversations
- Cost monitoring
- Error logging

---

## Enhancement Ideas (For Extra Credit)

1. **Support Multiple File Types**
   - Add PDF support (PyPDF2)
   - Add DOCX support (python-docx)

2. **Improve UX**
   - Show document preview
   - Display confidence scores
   - Multi-turn conversation history

3. **Advanced Features**
   - Document summarization
   - Key topic extraction
   - Similar document recommendations

4. **Performance**
   - Cache embeddings for repeated documents
   - Implement rate limiting
   - Use async processing

5. **Security**
   - Use environment variables for API keys
   - Implement session-based storage
   - Add request logging

---

## Useful Resources

### Documentation
- [LangChain Docs](https://python.langchain.com/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [OpenAI API Docs](https://platform.openai.com/docs/api-reference)
- [Chroma Docs](https://docs.trychroma.com/)

### Tutorials
- [LangChain Q&A Tutorial](https://python.langchain.com/docs/use_cases/qa_structured_data/sql)
- [Streamlit Getting Started](https://docs.streamlit.io/library/get-started)
- [Embeddings Guide](https://platform.openai.com/docs/guides/embeddings)

### Related Concepts
- Vector embeddings and similarity search
- Semantic search vs. keyword search
- RAG (Retrieval-Augmented Generation)
- Prompt engineering

---

## Submission Checklist

- [ ] `app.py` - Application code
- [ ] `requirements.txt` - Dependencies
- [ ] `SETUP_GUIDE.md` - Instructions
- [ ] Tested locally ✓
- [ ] No hardcoded API keys ✓
- [ ] Clear documentation ✓
- [ ] README or notes on how to run
- [ ] (Optional) GitHub repo link
- [ ] (Optional) Streamlit Cloud deployment link

---

## Support & Questions

If you encounter issues:

1. **Check SETUP_GUIDE.md** - Troubleshooting section
2. **Verify dependencies** - `pip install -r requirements.txt`
3. **Check OpenAI account** - Billing enabled, API key valid
4. **Read error messages** - Usually indicate what's missing
5. **Test with sample** - Use provided state_of_the_union.txt example

---

## Final Notes

This assignment covers essential skills for AI development:
- ✓ Working with LLMs via APIs
- ✓ Vector embeddings and similarity search
- ✓ Building retrieval-augmented systems
- ✓ Creating web applications with Python
- ✓ Production-ready code organization

The "Ask the Doc" pattern is used in real-world applications:
- Customer support chatbots
- Internal documentation search
- Research paper analysis
- Legal document review
- Medical literature search

Good luck! 🦜🔗

---

**Created:** 2026-04-26  
**Course:** Programming for Data Analytics / AI Applications / Web Development  
**Week:** 15  
**Points:** 10
