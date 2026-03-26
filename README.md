# 📄 Legal Document QA System

## 🚀 Overview

This project is a Retrieval-Augmented Generation (RAG) based Legal Document Assistant. It allows users to upload multiple PDF documents and ask questions based on their content.

## ⚙️ Tech Stack

* Gradio (UI)
* LangChain (Orchestration)
* FAISS (Vector Database)
* HuggingFace MiniLM (Embeddings)
* Groq API (LLaMA 3.1 Model)

## 🔄 Workflow

1. Upload PDF(s)
2. Validate Legal Documents
3. Split into chunks
4. Generate embeddings
5. Store in FAISS
6. Retrieve relevant chunks
7. Generate answer using LLM

## ▶️ How to Run

```bash
pip install -r requirements.txt
python app.py
```

## 🔐 Environment Variable

```bash
export GROQ_API_KEY="your_api_key"
```

## 📌 Features

* Multiple PDF upload
* Legal document validation
* Semantic search (FAISS)
* Fast LLM responses via Groq

## 📷 Demo

(Add screenshots here)

## 👨‍💻 Author

Jitesh Bairagi
