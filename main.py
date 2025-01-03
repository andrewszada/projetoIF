import produto

def menu_principal():
    print("_______________________________________")
    print("__     Sistema de Gestão de Loja      _____")
    print("_______________________________________")
    print("_____  2 - Módulo Produto/Vendas  _____")    
    print("_____  5 - Módulo Fornecedores    _____")
    print("_____  0 - Sair                   _____")
    op_princ = input("##### Escolha sua opção: ")
    return op_princ

match op_princ:
    case 1:
        produto.modulo_produto()
        