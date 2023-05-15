
class Produto:

    def __init__(self, id, nome, peso, preço, estoque) -> None:
        
        self._id = id
        self._nome = nome
        self._peso = peso
        self._preço = preço
        self._estoque = estoque

    def sqlInserirProduto(self):

        sql = f'''
        
        INSERT INTO "Produtos"
        Values(default, '{self._nome}', '{self._peso}', '{self._preço}', '{self._estoque}')

        '''

        return sql
    
    def sqlAtualizarProduto(self):

        sql = f'''

        UPDATE "Produtos"
        SET
        "Nome" = '{self._nome}', "Peso" = '{self._peso}', "Preço" = '{self._preço}', "Estoque" = '{self._estoque}'
        WHERE "Id" = {self._id}
        
        '''

        return sql
    