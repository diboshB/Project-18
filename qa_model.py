# qa_model.py

from transformers import pipeline

# Initializing the Hugging Face QA pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", tokenizer="deepset/roberta-base-squad2")

print("QA model loaded successfully.")
