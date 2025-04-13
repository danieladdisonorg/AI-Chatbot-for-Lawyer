import streamlit as st

uploaded_files = st.file_uploader("Upload files", type=["pdf"], accept_multiple_files=True)

user_Query = st.text_area("Enter your query here: " , height=150, placeholder="Type your query here...")

ask_button = st.button("Ask AI Assistant")


if ask_button:
   if uploaded_files:
      st.chat_message("User", avatar="👤").write(user_Query)
      st.chat_message("AI Assistant", avatar="🤖").write("Fixed Response")
   else:  
      st.warning("Please upload a PDF file to proceed.")
       
      
      
