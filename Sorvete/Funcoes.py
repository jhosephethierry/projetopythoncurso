from classCliente import Cliente
from classProduto import Produto
from classSabores import Sabor 
from classPedido import Pedido


import psycopg2


def consultarBanco(sql):

    conn = psycopg2.connect(dbname = "Sorvete", host = "localhost", port = "5432", user = "postgres", password = "postgres")

    cursor = conn.cursor()
    cursor.execute(sql)
    resultado = cursor.fetchall()
    cursor.close()
    conn.close()

    return resultado
    
def manipularBanco(sql):
        
    conn = psycopg2.connect(dbname = "Sorvete", host = "localhost", port = "5432", user = "postgres", password = "postgres")
    cursor = conn.cursor()

    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()



def visualizarClientes():


    clientes = consultarBanco('''

    SELECT * FROM "Clientes"
    ORDER BY "Id" ASC

    ''')
    

    if clientes:

        print("Estes são os clientes cadastrados.")
        print("")

        for cliente in clientes:
            print(f'''
            ID - {cliente[0]}
            Nome - {cliente[1]}
            ''')
            
    else:
        
        print("Não há clientes cadastrados.")

    input("Enter...")

def visualizarProdutos():

    produtos = consultarBanco('''

    SELECT * FROM "Produtos"
    ORDER BY "Id" ASC

    ''')

    if produtos:

        print("Estes são os produtos cadastrados.")
        print("")

        for produto in produtos:
            print(f'''
                ID - {produto[0]} | Categoria - {produto[1]} | Sabor - {produto[2]} | Peso - {produto[3]} | Preço - R$ {produto[4]} | Estoque - {produto[5]}''')
            
        input("Enter...")

    else:
        
        print("Não há produtos cadastrados.")

    print("")


def visualizarSabores():

    sabores = consultarBanco('''

    SELECT * FROM "Sabores"
    ORDER BY "Id" ASC

    ''')

    if sabores:

        print("Estes são os sabores cadastrados.")
        print("")

        for sabor in sabores:
            print(f'''
                Id - {sabor[0]} | Sabor - {sabor[1]}''')
            
        input("Enter...")

    else:
        
        print("Não há sabores cadastrados.")

    print("")


def visualizarPedidos():

    pedidos = consultarBanco('''

    SELECT * FROM "Pedidos"
    ORDER BY "Id" ASC

    ''')

    input("Enter...")

    if pedidos:

        print("Estes são os pedidos cadastrados:")
        print("")

        for pedido in pedidos:

            produto = consultarBanco(f'''
         
            SELECT * FROM "Produtos"
            WHERE
            "Id" = {pedido[2]}
         
         ''')[0]


            cliente = consultarBanco(f'''
         
            SELECT * FROM "Clientes"
            WHERE
            "Id" = {pedido[1]}
         
         ''')[0]

            print(f'''
            
            ID - {pedido[0]}
            Nome do Cliente - {cliente[1]}
            ID do Produto - {pedido[2]}
            Produto - {produto[1]}
            Sabor - {produto[2]}
            Quantidade - {pedido[3]}
            Valor - R${pedido[4]},00
            Data e Hora -  {pedido[5]}
            
            
            ''')
        input("Enter...")
    else:
        
        print("Não há pedidos cadastrados.")



def inserirCliente():

    print("Cadastro de Cliente")

    cliente = Cliente(None, input("Digite o nome do cliente. "))

    manipularBanco(Cliente.sqlInserirCliente(cliente))

    print("Novo cliente inserido com sucesso!")
    print("")


    op = input("Quer continuar inserindo clientes? s ou n? ")
    
    match op:

        case "s":
            inserirCliente()
        case "n":
            print("Saindo!")
            print("")
        case _:
            print("Digite uma opção válida.")
            print("")   
        
    
    op = input("Quer visualizar seus clientes? s ou n? ")
    
    match op:

        case "s":
            visualizarClientes()
        case "n":
            print("Saindo!")
            print("") 
        case _:
            print("Digite uma opção válida.")
            print("")
    


def inserirProduto():

    print("Cadastro de Produto")

    produto = Produto(None, input("Digite o nome do produto. "), visualizarSabores(), input("Digite o peso. "), input("Digite o preço. R$ "), input("Digite o estoque. "))

    manipularBanco(produto.sqlInserirProduto())

    print("Novo produto inserido com sucesso!")


    op = input("Quer continuar inserindo produtos? S/N ")
    
    match op.upper():

        case "S":
            inserirProduto()
        case "N":
            print("Saindo!")
            print("")
        case _:
            print("Digite uma opção válida.")
            print("")   
        
    
    op = input("Quer visualizar seus produtos? s ou n? ")
    
    match op:

        case "s":
            visualizarProdutos()
        case "n":
            print("Saindo!")
            print("") 
        case _:
            print("Digite uma opção válida.")
            print("")



def inserirSabores():

    print("Cadastro de Sabores")

    sabor = Sabor(None, input("Digite o nome do sabor. "))

    manipularBanco(Sabor.sqlInserirSabor(sabor))

    print("Novo sabore inserido com sucesso!")
    print("")


    op = input("Quer continuar inserindo sabores? s ou n? ")
    
    match op:

        case "s":
            inserirSabores()
        case "n":
            print("Saindo!")
            print("")
        case _:
            print("Digite uma opção válida.")
            print("")   
        
    
    op = input("Quer visualizar seus clientes? s ou n? ")
    
    match op:

        case "s":
            visualizarSabores()
        case "n":
            print("Saindo!")
            print("") 
        case _:
            print("Digite uma opção válida.")
            print("")

def escolherSabor():

    print("Estes são os sabores disponíves.")

    visualizarSabores()



def inserirPedido():

    print("Cadastro de Pedido")
    
    

    pedido = Pedido(None, input("Digite o id do cliente. "), input("Digite o id do produto. "), input("Digite a quantidade. "), None, None)

    produtoEscolhido = consultarBanco(f'''
    SELECT * FROM "Produtos"
    WHERE "Id" = {pedido._idProduto}
    ''')[0]

    produto = Produto(produtoEscolhido[0], produtoEscolhido[1], produtoEscolhido[2], produtoEscolhido[3],produtoEscolhido[4])

    if int(produto._estoque) < int(pedido._quantidade):
        print("Não há estoque suficiente.")
        return "Não há estoque suficiente."
    else: 
        produto._estoque = int(produto._estoque) - int(pedido._quantidade)

    pedido._valorTotal = float(produto._preço) * float(pedido._quantidade)

    manipularBanco(pedido.sqlInserirPedido())

    manipularBanco(produto.sqlAtualizarProduto())

    print(f"Compra de {pedido._quantidade} Sorvetes de {produto._nome} por R$ {pedido._valorTotal} foi cadastrada com sucesso!")
    input("Enter...")

def atualizarCliente():

    visualizarClientes()

    id = input("Digite o id do cliente que deseja atualizar: ")
    nome = input("Digite o novo nome do cliente: ")

    manipularBanco(f'''
    
    UPDATE "Clientes"
    SET
        "Nome" = '{nome}'
    WHERE 
        "Id" = {id}

    ''')
    print("Cliente Atualizado com sucesso!")
    input("Enter...")

def atualizarProduto():

    visualizarProdutos()

    id = input("Digite o id do produto que deseja atualizar: ")
    nome = input("DIgite o nome do produto: ")
    peso = input("Digite o peso do produto: ")
    preço = input("Digite o preço do produto: ")
    estoque = input("Digite o estoque do produto: ")

    manipularBanco(f'''
    
    UPDATE "Produtos"
    SET
       "Nome" = '{nome}'     
       "peso" = {peso}     
       "preço" = {preço}    
       "estoque" = {estoque}  
    WHERE
        "Id" = {id}      
    
    ''')
    input("Enter...")

def atualizarPedido():

    visualizarPedidos()

    id = input("Digite o id do pedido que deseja atualizar: ")
    idCliente = input("Digite o id do Cliente que deseja atualizar: ")
    idProduto = input("Digite o id do Produto que deseja atualizar: ")
    qtd = input("Digite a quantidade do produto: ")
 
    manipularBanco(f'''
    
    UPDATE "Pedidos"
    SET
       "Id_Cliente" = {idCliente}     
       "Id_Produto" = {idProduto}     
       "Quantidade" = {qtd}      
    WHERE
        "Id" = {id}      
    
    ''')    
    print("Pedido atualizado com sucesso!")
    input("Enter...")

def deletarCliente():

    visualizarClientes()

    id = input("Digite o id do cliente que deseja excluir: ")

    manipularBanco(f'''
    
    DELETE FROM "Clientes"
    WHERE 
    "Id" = {id}

    ''')    
    print("Cliente excluido com sucesso!")
    input("Enter...")

def deletarProduto():

    visualizarProdutos()

    id = input("Digite o id do produto que deseja excluir: ")

    manipularBanco(f'''
    
    DELETE FROM "Produtos"
    WHERE 
    "Id" = {id}

    ''')    
    print("Produto excluido com sucesso!")
    input("Enter...")

def deletarPedido():

    visualizarPedidos()

    id = input("Digite o id do cliente que deseja excluir: ")

    manipularBanco(f'''
    
    DELETE FROM "Pedidos"
    WHERE 
    "Id" = {id}

    ''')    
    print("Pedido excluido com sucesso!")
    input("Enter...")