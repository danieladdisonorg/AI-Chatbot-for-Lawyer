from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from vector_db import faiss_db
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file
load_dotenv()
grok_api_key = os.getenv("GROK_API_KEY")
llm_model = ChatGroq(model="llama3-70b-8192", api_key=grok_api_key, temperature=0.1, max_tokens=1000)

# Retrieve Documents
def retrieve_docs(query, uploaded_files=None):
    try:
        if uploaded_files:
            # Update FAISS index with uploaded PDFs (handled in vector_db.py)
            from vector_db import update_faiss_index
            update_faiss_index(uploaded_files)
        return faiss_db.similarity_search(query, k=4)  # Retrieve top 4 documents
    except Exception as e:
        print(f"Error retrieving documents: {e}")
        return []

def get_context(documents):
    try:
        context = "\n\n".join([doc.page_content for doc in documents])
        return context
    except Exception as e:
        print(f"Error getting context: {e}")
        return ""

custom_prompt = """
Answer the user's query using only the provided context. If no relevant information is found, generate a plausible answer.
Query: {query}
Context: {context}
Answer:
"""

def ans_query(documents, model, query):
    try:
        context = get_context(documents)
        prompt = ChatPromptTemplate.from_template(custom_prompt)
        chain = prompt | model
        response = chain.invoke({"query": query, "context": context})
        return response.content  # Extract the text content
    except Exception as e:
        print(f"Error generating answer: {e}")
        return "An error occurred while generating the answer."