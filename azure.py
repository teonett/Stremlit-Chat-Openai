###############################################################
# +=========================================================+ #
# |     Openai + Azure  Web Interface Using Streamlit       | #
# +=========================================================+ #
# | Author   : JOSE TEOTONIO DA SILVA NETO [TEO]            | #
# | Objective: Build a example of streamlit web app         | #
# | Version  : 1.0.0.0                                      | #
# +=========================================================+ #
# | Name   | Changed At | Description                       | #
# +=========================================================+ #
# | Teo    | 20/11/2023 | Build Starter Version             | #
# +=========================================================+ #
# | Libraries Extras To Solve Encoding Issues               | #
# +=========================================================+ #
# | pip install chardet                                     | #
# | conda install -c conda-forge charset-normalizer         | #
# +=========================================================+ #
###############################################################
import os
import openai
import streamlit as st
from dotenv import load_dotenv

# Configuração da página
st.set_page_config(
    page_title="Chat Azure",
    page_icon="🤖",
)
st.title("Chat Usando OpenAI Azure")

# +=========================================================+ #
# | Internal Environment Parameters                         | #
# +=========================================================+ #
load_dotenv()
openai.api_type = os.environ['AZURE_API_TYPE']
openai.api_base = os.environ['AZURE_URL_BASE']
openai.api_version = os.environ['AZURE_API_VERSION']
openai.api_key = os.environ['AZURE_API_KEY']

# +=========================================================+ #
# | Logic [Read, Interprete and Response]                   | #
# +=========================================================+ #
def response_api(messages):
    try:
        response = openai.ChatCompletion.create(
            engine=os.environ['AZURE_ENGINE_NAME'],
            messages=messages
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Erro na chamada da API: {e}")
        return None

# +=========================================================+ #
# | Form Layout To Ask And Retrieve Answer(s)               | #
# +=========================================================+ #
with st.form("my_form"):
    st.write("Faça uma pergunta:")
    question = st.text_area("Sua Pergunta")

    submitted = st.form_submit_button("Submit")

    if submitted and question.strip() != "":
        # +=========================================================+ #
        # | Answer From API                                         | #
        # +=========================================================+ #
        user_message = {"role": "user", "content": question}
        system_message = {"role": "system", "content": "Assistant is a large language model trained by OpenAI."}
        messages = [system_message, user_message]

        result = response_api(messages)

        if result is not None:
            # +=========================================================+ #
            # | Add Template Response as Message                                        | #
            # +=========================================================+ #
            st.success("Resposta:")
            st.info(result)
            messages.append({"role": "assistant", "content": result})
        else:
            st.warning("Não foi possível recuperar uma resposta")

# +=========================================================+ #
# | Show Up Result Message  - Local Consult                 | #
# +=========================================================+ #
if "messages" in locals():
    st.write("Conversa:")
    for message in messages:
        st.text(f"{message['role'].capitalize()}: {message['content']}")
