
class Produto:

    def __init__(self, id, nome, sabor, peso, preço, estoque) -> None:
        
        self._id = id
        self._nome = nome
        self._sabor = sabor
        self._peso = peso
        self._preço = preço
        self._estoque = estoque

    def sqlInserirProduto(self):

        sql = f'''
        
        INSERT INTO "Produtos"
        Values(default, '{self._nome}', '{self._sabor}', '{self._peso}', '{self._preço}', '{self._estoque}')

        '''

        return sql
    
    def sqlInserirSabor(self):

        sql = f'''
        
        INSERT INTO "Sabores"
        Values(default, '{self._sabor}')

        '''

        return sql
    
    def sqlAtualizarProduto(self):

        sql = f'''

        UPDATE "Produtos"
        SET
        "Nome" = '{self._nome}', Sabor = '{self._sabor}', "Peso" = '{self._peso}', "Preço" = '{self._preço}', "Estoque" = '{self._estoque}'
        WHERE "Id" = {self._id}
        
        '''

        return sql
    