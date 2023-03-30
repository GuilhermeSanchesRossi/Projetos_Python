from src.controllers.usuario_controller import UsuarioController
from src.controllers.produto_controller import ProdutoController
from src.dao.produto_dao import ProdutoDAO
from src.dao.usuario_dao import UsuarioDAO
from src.models.usuario import Usuario
from src.models.produto import Produto

prod_controller = ProdutoController()
prod_teste = Produto("2", "Pokémon Scarlet", 249.90, "Mais um jogo de Pokémon que repete a mesma fórmula que todo mundo já tá de saco cheio")
prod_controller.cadastrar_prod(prod_teste)
get_prod = prod_controller.procurar_prod("2")
print(get_prod.get_id())
print(get_prod.get_nome())