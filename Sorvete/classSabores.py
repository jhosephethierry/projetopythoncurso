from classConexao import Conexao

class Sabor:

    def __init__(self, id, sabor) -> None:
        
        self._idSabor = id
        self._sabor = sabor
        
    def sqlInserirSabor(self):

        sql = f'''
        
        INSERT INTO "Sabores"
        Values(default, '{self._sabor}')

        '''

        return sql