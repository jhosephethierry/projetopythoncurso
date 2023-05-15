from classCliente import Cliente
from classProduto import Produto
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
            print(f"{cliente[0]} | Nome - {cliente[1]}")

    else:
        
        print("Não há clientes cadastrados.")

    print("")

def visualizarProdutos():

    produtos = consultarBanco('''

    SELECT * FROM "Produtos"
    ORDER BY "Id" ASC

    ''')

    if produtos:

        print("Estes são os produtos cadastrados.")
        print("")

        for produto in produtos:
            print(f"{produto[0]} | Sabor - {produto[1]} | Peso - {produto[2]} | Preço - R$ {produto[3]} | Quantidade - {produto[4]}")
    
    else:
        
        print("Não há produtos cadastrados.")

    print("")

def visualizarPedidos():

    pedidos = consultarBanco('''

    SELECT * FROM "Pedidos"
    ORDER BY "Id" ASC

    ''')

    if pedidos:

        print("Estes são os pedidos cadastrados.")
        print("")

        for pedido in pedidos:
            print(f"{pedido[0]} | {pedido[1]} | {pedido[2]} | {pedido[3]} | {pedido[4]} | {pedido[5]}")

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

    produto = Produto(None, input("Digite o nome do produto. "), input("Digite o peso. "), input("Digite o preço. R$ "), input("Digite o estoque. "))

    manipularBanco(produto.sqlInserirProduto())

    print("Novo produto inserido com sucesso!")


    op = input("Quer continuar inserindo produtos? s ou n? ")
    
    match op:

        case "s":
            inserirProduto()
        case "n":
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



def inserirPedido():

    print("Cadastro de Pedido")

    pedido = Pedido(None, input("Digite o id do cliente. "), input("Digite o id do produto. "), input("Digite a quantidade. "), None, None)

    print("Pedido cadastrado com sucesso!")

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
def atualizarPedido():

    visualizarPedidos()

    id = input("Digite o id do produto que deseja atualizar: ")
    qtd = input("Digite a quantidade do produto: ")
    

    manipularBanco(f'''
    
    UPDATE "Pedidos"
    SET
       "Nome" = '{nome}'     
       "peso" = {peso}     
       "preço" = {preço}    
       "estoque" = {estoque}  
    WHERE
        "Id" = {id}      
    
    ''')    
