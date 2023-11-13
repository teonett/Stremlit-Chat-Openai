###############################################################
# +=========================================================+ #
# |        AI Powered by Openai Api and Streamlit           | #
# +=========================================================+ #
# | Author   : JOSE TEOTONIO DA SILVA NETO [TEO]            | #
# | Objective: Build a simple char using openai Api         | #
# | Version  : 1.0.0.0                                      | #
# +=========================================================+ #
# | Name   | Changed At | Description                       | #
# +=========================================================+ #
# | Teo    | 11/11/2023 | Build Starter Version             | #
# +=========================================================+ #
###############################################################

# +=========================================================+ #
# | Libraries necessaries to execute current project        | #
# +=========================================================+ #
import streamlit as st 
from langchain.llms import OpenAI

# +=========================================================+ #
# | Page Title of current project                           | #
# +=========================================================+ #
st.set_page_config(page_title='Chat Usando Openai')
st.title("Chat Usando Openai Api")

openai_api_key = st.sidebar.text_input("OpenAI API Key")

# +=========================================================+ #
# | App Logic [Read, Interprete and Response]               | #
# +=========================================================+ #
def response(input_text):
    llm = OpenAI(temperature = 0.2, 
                 openai_api_key = openai_api_key, )
    st.info(llm(input_text))

with st.form("my_form"):
    text = st.text_area("Qual a sua pergunta:", 
                "O que é IA usando NLP?")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Insira uma OpenAI API key válida!", icon= "⚠️")
    if submitted and openai_api_key.startswith("sk-"):
        response(text)
