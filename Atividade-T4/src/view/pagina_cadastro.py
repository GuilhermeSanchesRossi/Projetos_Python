import streamlit as st
from controllers.usuario_controller import UsuarioController
from models.usuario import Usuario

class PaginaCadastro:

    def __init__(self):
        #sei que não faz sentido pedir para um user inserir um id, é só pra testar o funcionamento do cadastro
        self._user_controller = UsuarioController()
        self.entradas_cadastro()
        self.fazer_cadastro()

    def criar_model(self):
        return Usuario(self._id, self._nome, self._email, self._senha)

    def fazer_cadastro(self):
        user_criado = self.criar_model()
        try:
            self._user_controller.cadastrar_user(user_criado)
            st.write('Cadastro feito com sucesso!')
        except:
            st.write('Cadastro falhou!')

    def entradas_cadastro(self):
        with st.form(key = 'entradas para cadastro'):
            self._id = st.text_input(label = "Insira um id")
            self._nome = st.text_input(label = "Insira um nome")
            self._email = st.text_input(label = "Insira seu email")
            self._senha = st.text_input(label = "Insira sua senha")
            self._bot_cadastrar = st.form_submit_button('Finalizar cadastro')
            if self._bot_cadastrar:
                self.fazer_cadastro()

    

    
