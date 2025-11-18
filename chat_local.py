
# Streamlit documentation
# Terminal se connecter à l'environnement chat_llm
# lancer chat _local

import streamlit as st
from llama_index.llms.ollama import Ollama

st.title("chat with toto")

llm = Ollama(
    model="toto1",
    request_timeout=60.0,
    # Manually set the context window to limit memory usage
    context_window=8000,
)

prompt = st.text_input("Your question")
if st.button("send"):
    resp = llm.complete(prompt)
    st.write(f"response from LLM is {resp}")