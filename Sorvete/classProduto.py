
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
        Values(default, '{self._nome}', '{self._sabor}', '{self._peso}', '{self._preço:.2f}', '{self._estoque}')

        '''

        return sql
    
    def sqlEscolherSabor(self):

        sql = f'''
        
        UPDATE "Produtos"
        SET
        "Sabor" = '{self._sabor}'
        WHERE "Id" = '{self._id}'

        '''

        return sql
    
    def sqlAtualizarEstoqueProduto(self):

        sql = f'''
        
        UPDATE "Produtos"
        SET
        "Estoque" = '{self._estoque}'
        WHERE "Id" = '{self._id}'

        '''

        return sql
    
    
    