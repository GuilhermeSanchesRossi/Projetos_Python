import streamlit as st
from PIL import Image
from src.models.produto import Produto
from src.controllers.produto_controller import ProdutoController

class PaginaHome:

    _produto_atual = None
    _prod_controller = None

    def __init__(self):
        st.title('Bem-vindo! Nosso catálogo:')
        self._Dk3_img = Image.open('src/view/DarkSouls3.jpg')
        st.image(self._Dk3_img)
        self._produto_DK3 = self.pegar_produto("1")
        st.write(self._produto_DK3.get_nome())
        st.write(self._produto_DK3.get_descricao())
        self._PKMN_img = Image.open('src/view/PokemonScarlet.jpg')
        st.image(self._PKMN_img)
        self._produto_PKMN = self.pegar_produto("2")
        st.write(self._produto_PKMN.get_nome())
        st.write(self._produto_PKMN.get_descricao())

    def pegar_produto(self, id):
        self._prod_controller = ProdutoController()
        self._produto_atual = self._prod_controller.procurar_prod(id)
        return self._produto_atual
