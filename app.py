# app.py

from fastapi import FastAPI
from pydantic import BaseModel
import nest_asyncio
import threading
import uvicorn
import logging
from langchain.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline

# Apply nest_asyncio for Jupyter notebook compatibility
nest_asyncio.apply()

# Suppress log messages
logging.basicConfig(level=logging.WARNING)

# Initialize FastAPI app
app = FastAPI()

# Define request model for incoming queries
class QueryRequest(BaseModel):
    question: str

# Initialize the QA pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")

# Load the FAISS vector store
embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = FAISS.load_local("./faiss_index", embedding_model, allow_dangerous_deserialization=True)

@app.post("/ask-question/")
async def ask_question(query_request: QueryRequest):
    query = query_request.question

    # Perform similarity search on the FAISS vector store
    search_results = vector_store.similarity_search(query, k=1)

    # Extract context from the top search result
    context = search_results[0].page_content  

    # Get the answer from the QA model
    answer = qa_pipeline(question=query, context=context)

    # Return the answer
    return {"answer": answer['answer']}

# Function to run FastAPI server in a separate thread
def run_fastapi():
    uvicorn.run(app, host="127.0.0.1", port=8007, log_level="info")

# Run the FastAPI app in a separate thread
thread = threading.Thread(target=run_fastapi)
thread.start()

print("FastAPI server started.")
