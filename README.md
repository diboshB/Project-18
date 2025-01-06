# Project-18
Capstone_Project - Generative AI - Chatbot


Problem Statement:
The objective of this project is to build a chatbot using Langchain
and Retrieval-Augmented Generation (RAG) techniques. The
chatbot will be designed to answer questions related to financial
and operational risk guidelines provided by the Reserve Bank of
India (RBI). These documents contain important information about
financial and operational risks that banks and financial institutions
must adhere to. The chatbot will assist users in navigating and
understanding the complex regulations and guidelines set forth by
the RBI, facilitating improved comprehension and decision-making.
Solution Approach:
The solution is built around several key steps:
1. Document Loading and Preprocessing:
• Input Data: The input for this chatbot is comprised of two
documents: "financial risk.pdf" and "operations risk.pdf", both
containing RBI’s guidelines.
• Document Loading: The documents are loaded using
Langchain’s PyPDFLoader. Each document is parsed and
converted into structured text.
• Text Splitting: Once loaded, the document content is split
into smaller chunks using
Langchain’s RecursiveCharacterTextSplitter to ensure
efficient processing. Each chunk is no longer than 1000
characters with an overlap of 100 characters to retain context
across chunks.
2. Embeddings Generation:
• Text Embeddings: The documents need to be converted into
numerical representations (embeddings) for efficient retrieval
during question answering. Initially, embeddings are
generated using the DistilBERT model for each document
chunk.
• Model Used: distilbert-base-uncased is used for generating
embeddings from the documents, which are then stored as
NumPy arrays.
• Alternative Model: The embeddings are further enhanced
using the Hugging Face all-MiniLM-L6-v2 model, which is
more suited for sentence-level embeddings and is integrated
with Langchain’s vector store (FAISS).
3. Storing Embeddings in a Vector Store:
• Vector Store Creation: The generated embeddings are
stored in a FAISS (Facebook AI Similarity Search) vector
store, which is used for fast similarity searches. This allows
the chatbot to find the most relevant document chunks in
response to a user query.
• Saving the FAISS Index: The FAISS index is saved locally
for later retrieval during inference.
4. Summarization:
• Context Summarization: In cases where the document
chunks exceed the maximum length for effective processing,
the context is summarized using Hugging
Face’s facebook/bart-large-cnn model. The summarizer
reduces the text to a concise form while retaining key
information.
• Contextual Representation: This summarization ensures
that even large documents can be represented in a way that
is suitable for efficient querying and retrieval.
5. Question-Answering Pipeline:
• Question-Answering (QA): A pre-trained question-
answering pipeline is used for processing user queries.
The distilbert-base-cased-distilled-squad model is used for
extracting answers from the summarized context.
• Pipeline Flow: The chatbot uses the vector store to search
for the most relevant chunks and then feeds these chunks to
the QA model to generate an answer based on the user's
question.
6. FastAPI Integration for Serving the Model:
• API Creation: The FastAPI framework is used to create an
API endpoint that allows users to interact with the chatbot. A
Pydantic model is used to handle the incoming questions as
part of the API request.
• Running FastAPI Server: The FastAPI app is run in a
separate thread using uvicorn, which serves the chatbot
model for real-time inference.
• Similarity Search: Each incoming query is used to perform
a similarity search on the FAISS vector store to retrieve
relevant document chunks that can be used as context for
generating an answer.
• Response Generation: The chatbot then generates and
returns an answer based on the context retrieved from the
vector store.
7. Testing the API:
• Client for API Testing: A simple Python script is used to test
the FastAPI server by sending HTTP POST requests with a user
query. The response from the chatbot is then printed to verify
the model’s performance in answering real-world queries.
Key Insights:
• Document Splitting: By splitting documents into
manageable chunks, the system ensures that it can handle
large documents without overwhelming the model’s input
limits. This step is critical for ensuring scalability when
working with lengthy financial regulations.
• Embedding Models: The choice of using a combination of
DistilBERT and all-MiniLM-L6-v2 ensures a balance between
computational efficiency and the quality of generated
embeddings, providing a high level of accuracy in similarity
searches.
• Summarization: Summarizing documents is essential to
handle long texts efficiently. By leveraging the facebook/bart-
large-cnn model, the system can ensure that users can
receive relevant answers even from complex documents with
large content.
• FastAPI: Integrating FastAPI enables the chatbot to be
served as a scalable API, allowing users to interact with the
model through a simple web interface. This makes the chatbot
easily accessible and usable for a wide range of queries.
Future Applications:
• Dynamic Update of Knowledge Base: As new RBI
guidelines are released, they can be easily incorporated into
the system by reloading the documents, re-generating
embeddings, and updating the FAISS vector store. This
makes the system highly adaptable to future changes in
regulations.
• Scalability for Other Regulatory Documents: The same
architecture can be extended to other regulatory frameworks
(e.g., SEBI, RBI, IRDAI) for creating similar chatbots for
different sectors, enhancing the versatility of the solution.
• Automated Compliance Checking: The chatbot can be
enhanced to assist financial institutions in ensuring
compliance with RBI regulations by checking user-submitted
queries against the relevant sections of the guidelines.
Conclusion:
This project successfully demonstrates the use of a chatbot to
assist users in navigating financial and operational risk guidelines
from the RBI. By leveraging Langchain’s document loaders,
embeddings generation, and FastAPI integration, the chatbot can
efficiently respond to complex queries, providing users with an
intelligent, automated assistant to understand and interpret RBI
regulations. The solution is scalable and adaptable, making it
suitable for future updates and the addition of other regulatory
frameworks.
