import gradio as gr
import os
from groq import Groq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

GROQ_API_KEY = "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"   

client = Groq(api_key=GROQ_API_KEY)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = None
processed_files = set()

LEGAL_KEYWORDS = [
    "agreement", "contract", "party", "clause", "liability",
    "terms", "conditions", "confidential", "jurisdiction",
    "law", "obligation", "warranty", "breach",
    "settlement", "nda", "lease", "intellectual property"
]

def is_legal_document(documents):
    try:
        text = " ".join([doc.page_content.lower() for doc in documents])
        match_count = sum(keyword in text for keyword in LEGAL_KEYWORDS)
        return match_count >= 3
    except:
        return False

def process_multiple_pdfs(files):
    all_chunks = []
    valid_files = []

    try:
        for file in files:
            loader = PyPDFLoader(file.name)
            documents = loader.load()

        
            if not is_legal_document(documents):
                continue

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=600,
                chunk_overlap=100
            )

            chunks = text_splitter.split_documents(documents)

            for chunk in chunks:
                chunk.metadata["source"] = file.name

            all_chunks.extend(chunks)
            valid_files.append(file.name)

        if not all_chunks:
            return None, " No valid legal PDFs uploaded."

        db = FAISS.from_documents(all_chunks, embeddings)

        return db, f" Processed {len(valid_files)} legal PDF(s)."

    except Exception as e:
        return None, f" Error processing PDFs: {str(e)}"

def chat_func(message, history, files):
    global vector_db, processed_files

    if not files:
        return " Please upload at least one PDF."

    try:
        file_names = set([f.name for f in files])

        if file_names != processed_files or vector_db is None:

            temp_db, status = process_multiple_pdfs(files)

            if temp_db is None:
                vector_db = None
                processed_files = set()
                return status

            vector_db = temp_db
            processed_files = file_names

        if vector_db is None:
            return " No valid legal documents available."

        results = vector_db.similarity_search(message, k=3)

        if not results:
            return " No relevant information found."

        context = "\n".join([doc.page_content for doc in results])

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": f"""
                    You are a Legal AI Assistant.
                    Answer ONLY from the given context.

                    Context:
                    {context}
                    """
                },
                {"role": "user", "content": message}
            ]
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f" Error: {str(e)}"


demo = gr.ChatInterface(
    fn=chat_func,
    title="📄 Multi-PDF Legal Assistant",
    description="Upload multiple legal PDFs and ask questions based on them.",
    additional_inputs=[
        gr.File(
            label="Upload Legal PDFs",
            file_types=[".pdf"],
            file_count="multiple"
        )
    ]
)


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 10000))  # ✅ change here

    demo.launch(
        server_name="0.0.0.0",
        server_port=port
    )
