import streamlit as st
from myFunctions import Gustavo
import pytest

st.set_page_config(
    page_title="Sherlock Links",
    page_icon=":telescope",
    layout="centered",
    initial_sidebar_state="expanded"
)

def main_page():
    st.markdown("# Sherlock Links 🔭")
    st.markdown('#### Gustavo Duarte e Silva')
    st.write('')
    st.image('https://media4.giphy.com/media/KAq5w47R9rmTuvWOWa/200.gif', width=300)

def descricao_projeto():
    Gustavo.DescricaoProjeto()

def buscar_url():
    st.markdown('# Sherlock Links 🔭')
    st.write('')
    try:
        url = st.text_input('Digite a URL para a busca: 🔍')
    except:
        st.error('Digite uma URL Valida')
    else:
        try:
            data_1 = Gustavo.Function([url])
            data_2 = Gustavo.Function(data_1)
            data_3 = Gustavo.Function(data_2)
            data_4 = Gustavo.Function(data_3)
            data_5 = Gustavo.Function(data_4)
            data_6 = Gustavo.Function(data_5)
            if type(data_1) is None:
                data_1 = [url]
            if type(data_2) is None:
                data_2 = [url]
            if type(data_3) is None:
                data_3 = [url]
            if type(data_4) is None:
                data_4 = [url]
            if type(data_5) is None:
                data_5 = [url]
            if type(data_6) is None:
                data_6 = [url]
            final = data_1 + data_2 + data_3 + data_4 + data_5 + data_6
            Gustavo.Recomendacao(final)
        except:
            st.error('Digite um URL Valida!!!')

paginas= {"Pagina Inicial": main_page, "Descrição do Projeto": descricao_projeto, "Buscar URL": buscar_url}

selected_page = st.sidebar.selectbox("Selecione a Pagina!", paginas.keys())
paginas[selected_page]()


