from src.models.produto import Produto
from src.dao.produto_dao import ProdutoDAO

class ProdutoController:

    def __init__(self) -> None:
        pass

    def cadastrar_prod(self, produto):
        ProdutoDAO.get_instance().cadastrar_produto(produto)

    def procurar_prod(self, id):
        return ProdutoDAO.get_instance().procurar_produto(id)
    