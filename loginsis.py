usuarios = []
senhas = []

def menu():
    ret = 0
    while ret != 3:
        print('1 - CADASTRO DE USUARIO')
        print('2 - VALIDACAO DE LOGIN')
        print('3 - SAIR DO SISTEMA')
        print('-' * 15)
        ret = int(input('SELECIONE UMA OPÇÃO: '))
        if ret == 1:
            return cadastro()
        if ret == 2:
            return login()
        if ret == 3:
            print('Saindo do sistema')
            break


def cadastro(): 
    usuario = input('Insira o nome do usuário: ')
    if usuario not in usuarios:
        usuarios.append(usuario)
        senha = input('Insira a senha do usuário: ')
        senhas.append(senha)
        return menu()
    else:
        print('O usuário já esta cadastrado')
        return menu()
    
def login():
    usuario_digitado = input('Nome do usuário: ')
    senha_digitada = input('Senha do usuário: ')
    if usuario_digitado in usuarios:
        for indice, usuario in enumerate(usuarios):
            if usuario_digitado == usuario and senha_digitada == senhas[indice]:
                print('Login bem sucedido')
    else:
        print('O Usuário não está cadastrado')
        return menu()


menu()
        
        
    

