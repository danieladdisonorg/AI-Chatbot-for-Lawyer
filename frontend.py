import streamlit as st
from rag_pipeline import ans_query, retrieve_docs, llm_model

# File uploader for PDFs
uploaded_files = st.file_uploader("Upload files", type=["pdf"], accept_multiple_files=True)

# Text area for user query
user_query = st.text_area("Enter your query here:", height=150, placeholder="Type your query here...")

# Button to trigger the query
ask_button = st.button("Ask AI Assistant")

if ask_button:
    if uploaded_files or user_query:
        st.chat_message("User", avatar="👤").write(user_query)
        try:
            documents = retrieve_docs(user_query, uploaded_files=uploaded_files)
            response = ans_query(documents=documents, model=llm_model, query=user_query)
            st.chat_message("AI Assistant", avatar="🤖").write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please upload a PDF file or enter a query to proceed.")