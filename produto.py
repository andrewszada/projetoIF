import validador
import pickle

def limpar_tela():
 os.system('cls' if os.name == 'nt' else 'clear')


def carregar_produtos():
    try:
        with open("produtos.dat", "rb") as arq_produtos:
            return pickle.load(arq_produtos)
    except FileNotFoundError:
        return {}

carrinho = {}
try:  
  arq_carrinho = open("carrinho.dat", "rb")
  produtos = pickle.load(arq_carrinho)
except:
  arq_carrinho = open("carrinho.dat", "wb")
  arq_carrinho.close()

produtos = {}
try:  
  arq_produtos = open("produtos.dat", "rb")
  produtos = pickle.load(arq_produtos)
except:
  arq_produtos = open("produtos.dat", "wb")
  arq_produtos.close()

def modulo_produto():
    op_produto = ''
    while op_produto != '0':
        limpar_tela()
        print("_______________________________________")
        print("_______           Módulo Produto_______")
        print("_______________________________________")         
        print("____  1 - Cadastrar Produto       _____")
        print("_____ 2 - Exibir Dados do Produto _____")
        print("_____ 3 - Alterar Dados do Produto ____")
        print("_____ 4 - Excluir Produto         _____")
        print("_____ 5 - Exibir produtos         _____")
        print("_____ 6 - Adicionar ao carrinho   _____")
        print("_____ 0 - Sair                    _____")
        op_produto = input("##### Escolha sua opção: ")
        return op_produto
    

def cadastrar_produtos():
    limpar_tela()
    print()
    print("____________________________________________")
    print("_____        Cadastrar Produto         _____")
    print("____________________________________________")
    print()
    id = str(len(produtos) + 1) ## codigo 
    nome_do_produto = input("Qual é o nome do produto desejado? ")
    while not validador.validar_nome(nome_do_produto):
        print("Nome de produto inválido. Por favor, insira apenas letras e espaços.")
        nome_do_produto = input("Qual o nome do produto ")
    else:
        print("Nome válido")
    
    quantidade_do_produto = input("Qual a quantidade do produto desejada: ")
    while not validador.aceitar_apenas_digitos(quantidade_do_produto):
        print("Quantidade de produto inválido, digite novamente")
        quantidade_do_produto = input("Qual a quantidade do produto desejada? ")
    else:
        print("Quantidade de produto válido")
    
    descricao = input("O que é esse produto? ")
    while not validador.aceitar_validar_nome(descricao):
        print("Nome de produto inválido. Por favor, insira apenas letras e espaços.")
        descricao = input("O que é esse produto? ")
    else:
        print("Valor válido")