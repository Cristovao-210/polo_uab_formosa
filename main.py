import streamlit as st
from streamlit_option_menu import option_menu
from paginas.paginas import *

st.set_page_config(page_title="Portal UAB Formosa", layout="wide")

# Menu lateral
with st.sidebar:
    selecionado = option_menu(
        menu_title="Navegação",
        options=["Início", "Cursos de Graduação", "Cursos de Especialização", "Contatos"],
        icons=["house", "book", "award", "envelope"],
        menu_icon="cast",
        default_index=0
    )
            
# Navegação das páginas
if selecionado == "Início":
    pagina_inicio()
elif selecionado == "Cursos de Graduação":
    pagina_graduacao()
elif selecionado == "Cursos de Especialização":
    pagina_especializacao()
elif selecionado == "Contatos":
    pagina_contatos()

