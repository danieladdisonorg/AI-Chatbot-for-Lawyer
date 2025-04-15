from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from vector_db import faiss_db

# Load environment variables from .env file
load_dotenv()
grok_api_key = os.getenv("GROK_API_KEY")
llm_model = ChatGroq(model="deepseek-r1-distill-llama-70b", api_key=grok_api_key, temperature=0.1, max_tokens=1000)


#  retrive Documents

def retrive_docs(query):
  try:
      return faiss_db.similarity_search(query)
  except Exception as e:
    print(f"Error retrieving documents: {e}")