# embedding.py

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
import os

# File paths for the PDF documents
pdf_paths = [
    "/Users/diboshbaruah/Capstone_Project - Generative AI/financial risk.pdf",
    "/Users/diboshbaruah/Capstone_Project - Generative AI/operations risk.pdf"
]

# Loading documents from PDFs
documents = []
for path in pdf_paths:
    loader = PyPDFLoader(path)
    documents.extend(loader.load())

# Splitting documents into smaller chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
chunks = text_splitter.split_documents(documents)

# Using Hugging Face's MiniLM model for embeddings
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Creating the FAISS vector store
vector_store = FAISS.from_documents(chunks, embedding_model)

# Saving the FAISS index to disk
vector_store.save_local("./faiss_index")

print("Embedding and FAISS index creation completed.")
