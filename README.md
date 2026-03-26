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

<img width="767" height="500" alt="interface1" src="https://github.com/user-attachments/assets/7d67ff98-102b-4e1f-a26e-681d3e92eb6b" />
<img width="767" height="500" alt="interface3" src="https://github.com/user-attachments/assets/98b42838-fd9d-4988-af33-cc3f2f4d4cb1" />



## 👨‍💻 Team Members

* Jogendar Das Bairagi
* ROSHAN BANKAR
* VIVEK GANGRADE
* MAAHI MAHESHWARI
* SHUBHANGI PRAJAPAT

