
class Pedido:
    
    def __init__(self, id, idCliente, idProduto, saborProduto, quantidade, valorTotal, timestamp):

        self._id = id
        self._idCliente = idCliente
        self._idProduto = idProduto
        self._saborProduto = saborProduto
        self._quantidade = quantidade
        self._valorTotal = valorTotal
        self._timestamp = timestamp

    def sqlInserirPedido(self):

        sql = f'''
        
        INSERT INTO "Pedidos"
        VALUES(default, '{self._idCliente}', '{self._idProduto}', '{self._saborProduto}', '{self._quantidade}', '{self._valorTotal}', default)
        
        '''

        return sql