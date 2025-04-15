from langchain_community.document_loaders import PDFPlumberLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS



# step1  
# upload & load raw pdf files
pdfs_dir = "pdfs/"

def upload_pdf(file):

 try:
  with open (pdfs_dir + file.name, "wb") as f:
    f.write(file.getbuffer())
 except Exception as e:
  print(f"Error uploading file: {e}")


def load_pdf(file_path):
    try:
     loader = PDFPlumberLoader(file_path)
     docment = loader.load()
     return docment
    except Exception as e:
      print(f"Error loading PDF: {e}")


file_path = 'UNO.pdf'
docment = load_pdf(file_path)
# print(f"Number of pages: {len(docment)}") 


# step2
#  create chunks

def create_chunks(docment):
   text_spitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200 , add_start_index=True)
   chunks = text_spitter.split_documents(docment)
   return chunks

text_chunk = create_chunks(docment)
# print(f"Number of chunks: {len(text_chunk)}")
      


# step3
# create embeddings  DeepSeek R1 with Ollama
ollama_model_name = "llama2:latest"
def embading_model(ollama_model_name):
  try:
    embanding = OllamaEmbeddings(model=ollama_model_name)
    return embanding 
  except Exception as e:
    print(f"Error creating embeddings: {e}")



# step4
FAISS_DB = 'vectorstore/db_faiss'
faiss_db = FAISS.from_documents(text_chunk, embading_model(ollama_model_name))
faiss_db.save_local(FAISS_DB)

