import time

contas = []

class ContaBancaria():

    id_conta = 1000
    

    def __init__(self, nome, sobrenome, cpf, saldo = 0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.saldo = saldo
        self.n_conta = ContaBancaria.id_conta + 1
        ContaBancaria.id_conta += 1

    def infoConta(self):
        return {'Nome Completo': self.nome + ' ' + self.sobrenome,
                'Nº da Conta': self.n_conta,
                'Saldo': self.saldo}

    def deposito(self):
        self.saldo = self.saldo + int(input('Insira o valor do depósito: R$'))


def novaConta():
    n = input('Qual o primeiro nome do usuário? ')
    sbn = input('Qual o sobrenome do usuário? ')
    cpf = input('Qual o CPF do usuário? ')
    conta = ContaBancaria(n, sbn, cpf)
    contas.append(conta)
    print('Nova conta criada ' + 'id: ' + str((ContaBancaria.id_conta)))
    time.sleep(2)
    menu()


def depositar():
    pList = int(input('Informe a posição da conta na lista: '))
    try:
        contas[pList].deposito()
        print('Deposito realizado com sucesso')
    except:
        print('Essa conta não existe')
    time.sleep(2)
    menu()

def transferir():
    valor = int(input('Valor da Transferência: R$'))
    pTransfer = int(input('Informe a posição da conta que vai transferir na lista: '))
    pReceb = int(input('Informe a posição da conta que vai receber na lista: '))
    try:
        contas[pTransfer].saldo = (contas[pTransfer].saldo -  valor)
        contas[pReceb].saldo = (contas[pReceb].saldo +  valor)
        print('Transferência realizada com sucesso !')
    except:
        print('Uma das contas é inexistente')
    time.sleep(2)


def lContas():
    print('Listagem de contas:  ')
    for i, conta in enumerate(contas):
        print('Posição', i)
        print(conta.infoConta())
    input('Aperte qualquer tecla para continuar')

def menu():
    ret = 0
    while ret != 5:
        print('BEM VINDO AO SISBANK, ESCOLHA UMA OPÇÃO')
        print('1 - NOVA CONTA')
        print('2 - INFORMAÇÕES DAS CONTAS')
        print('3 - DEPOSITAR')
        print('4 - TRANSFERIR')
        print('5 - SAIR')
        ret = int(input('Escolha uma opção '))
        if ret == 1:
            novaConta()
        elif ret == 2:
            lContas()
        elif ret == 3:
            depositar()
        elif ret == 4:
            transferir()
        elif ret == 5:
            exit()
        else:
            print('Valor inválido, insira um valor de 1 a 5')
            menu()

menu()
            


    
    

        
        



    