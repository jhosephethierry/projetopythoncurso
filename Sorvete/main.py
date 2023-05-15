import Funcoes as Func
import psycopg2

while True:

    try:
        print('''
        
    Sorvetes Sorriso

    Escolha uma opção no menu abaixo.
    1. Inserir Cliente | 2. Inserir Produto | 3. Inserir Pedido | 4. Visualizar Clientes | 5. Visualizar Produtos | 6. Visualizar Pedidos | 0. Sair

        ''')   

        op = input("Digite uma das opções. ")
        print("")
        
        match op:

            case "1":
                Func.inserirCliente()
            
            case "2":
                Func.inserirProduto()

            case "3":
                Func.inserirPedido()

            case "4":
                Func.visualizarClientes()

            case "5":
                Func.visualizarProdutos()

            case "6":
                Func.visualizarPedidos()

            case "0":
                print("Saindo...")
                break
            
            case _:
                print("Digite uma opção válida.")

        input("Digite Enter para continuar.")

    except(Exception, psycopg2.Error) as error:
        print(error)
