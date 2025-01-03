
def aceitar_apenas_digitos(*args):
    for arg in args:
        if not isinstance(arg, str) or not arg.isdigit():
            return False
    return True

def validar_nome(nome):
    # Esta função verifica se o nome contém apenas letras e espaços
    if nome.replace(" ", "").isalpha():
        return True
    else:
        print("Nome inválido. Por favor, insira apenas letras e espaços.")
        return False