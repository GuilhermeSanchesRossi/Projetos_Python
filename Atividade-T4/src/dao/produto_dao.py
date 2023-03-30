import sqlite3
from src.models.produto import Produto

class ProdutoDAO:

    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProdutoDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)

    def cadastrar_produto(self, produto):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Produtos (id, nome, preco, descricao)
            VALUES(?,?,?,?);
        """, (produto.get_id(), produto.get_nome(), produto.get_preco(), produto.get_descricao()))
        self.conn.commit()
        self.cursor.close()

    def procurar_produto(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Produtos
            WHERE id = '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = Produto(id=resultado[0], nome=resultado[1], preco=resultado[2], descricao=resultado[3])
        self.cursor.close()
        return item
