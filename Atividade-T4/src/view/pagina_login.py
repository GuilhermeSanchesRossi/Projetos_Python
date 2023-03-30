import streamlit as st
from controllers.usuario_controller import UsuarioController
from view.pagina_home import PaginaHome
from view.pagina_cadastro import PaginaCadastro

class PaginaLogin:

    _user_controller = None

    def __init__(self):
        self._user_controller = UsuarioController()
        st.title("Faça seu login")
        self._email = st.text_input(label = "email")
        self._senha = st.text_input(label = "senha")
        self.login_button()
        self.cadastro_button()

    def login_button(self):
        if st.button('Fazer login'):
            login_sucess = self.validar_login()

    def cadastro_button(self):
        if st.button('Realizar cadastro'):
            pag_cadastro = PaginaCadastro()

    def validar_login(self) -> bool:
        if (self._user_controller.comparar_Email(self._email) == False) and (self._user_controller.comparar_Senha(self._senha) == False):
            return False
        else:
            self._home_page = PaginaHome()
            return True