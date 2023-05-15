import Funcoes as Func
import psycopg2

while True:

    try:
        print('''
        
    Sorvetes Sorriso

    Escolha uma opção no menu abaixo.
    1. Menu Clientes  
    2. Menu Produtos 
    3. Menu Pedidos  
    0. Sair

        ''')   

        op = input("Digite uma das opções. ")
        print("")
        
        match op:

            case "1":

                while True:
                    print('''
                    
                    1 - Inserir Cliente
                    2 - Ver Clientes
                    3 - Atualizar Cliente
                    0 - Voltar ao menu principal
                    
                    ''')
                    op = input("Digite uma opção: ")

                    match op:
                        case "1": 
                            Func.inserirCliente()
                        case "2":
                            Func.visualizarClientes()
                        case "3":
                            Func.atualizarCliente()
                        case "0":
                            breakpoint        
            case "2":
                
                while True:
                    print('''
                    
                    1 - Inserir Produto
                    2 - Ver Produtos
                    3 - Atualizar Produto
                    0 - Voltar ao menu principal
                    
                    ''')
                    op = input("Digite uma opção: ")

                    match op:
                        case "1": 
                            Func.inserirProduto()
                        case "2":
                            Func.visualizarProdutos()
                        case "3":
                            Func.atualizarProduto()
                        case "0":
                            breakpoint

            case "3":
                
                while True:
                    print('''
                    
                    1 - Inserir Pedido
                    2 - Ver Pedidos
                    3 - Atualizar Pedido
                    0 - Voltar ao menu principal
                    
                    ''')
                    op = input("Digite uma opção: ")

                    match op:
                        case "1": 
                            Func.inserirPedido()
                        case "2":
                            Func.visualizarPedidos()
                        case "3":
                            Func.atualizarPedido()
                        case "0":
                            breakpoint
            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Digite uma opção válida.")

        input("Digite Enter para continuar.")

    except(Exception, psycopg2.Error) as error:
        print(error)
