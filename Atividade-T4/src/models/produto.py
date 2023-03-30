class Produto:

    def __init__(self, id, nome, preco, descricao):
        self._id = id
        self._nome = nome
        self._preco = preco
        self._descricao = descricao

    def get_id(self):
        return self._id

    def get_nome(self):
        return self._nome

    def get_preco(self):
        return self._preco
    
    def get_descricao(self):
        return self._descricao