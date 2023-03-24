import os
print('*' * 25); print('Menu de Criação de Carros'); print('*' * 25)
carros = []

class Carro:

    nome = ''
    pot = 0
    velMax = 0
    ligado = False

    def __init__(self, nome, pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot)*2
        self.ligado = False

    def info(self):
        print('Nome.....:' + self.nome)
        print('Potência.....' + str(self.pot))
        print('Vel.Maxima.:' + str(self.velMax))
        print('Ligado.....:' + ('sim' if self.ligado==True else 'Não'))

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

def Menu():
    print('1 - Novo Carro')
    print('2 - Informações do Carro')
    print('3 - Excluir Carro')
    print('4 - Ligar o Carro')
    print('5 - Desligar o Carro')
    print('6 - Listar Carro')
    print('7 - Sair')
    print('Quantidade de carros: ' + str(len(carros)))
    opc = int(input('Digite uma opção: '))
    return opc

def NovoCarro():
    n = input('Nome do Carro.....: ')
    p = input('Potencia do Carro....: ')
    car=Carro(n, p)
    carros.append(car)
    print('Novo Carro criado')
    os.system('pause')

def Informacoes():
    n = input('Informe o número do carro que deseja ver as informacoes: ')
    try:
        carros[int(n)].info()
    except:
        print('Esse carro não existe')
    os.system('pause')

def excluirCarro():
    n = input('Informe o número do carro que deseja excluir ')
    try:
        del carros[int(n)]
    except:
        print('Esse carro não existe')
    os.system('pause')

def ligarCarro():
    n = input('Informe o número do carro que deseja ligar: ')
    try:
        carros[int(n)].ligar()
    except:
        print('Esse carro não existe')
    os.system('pause')

def desligarCarro():
    n = input('Informe o número do carro que deseja desligar: ')
    try:
        carros[int(n)].desligar()
    except:
        print('Esse carro não existe')
    os.system('pause')


def ListarCarros():
    p=0
    for c in carros:
        print(str(p) + '-' + c.nome)
        p = p + 1
    os.system('pause')

ret = Menu()
while ret < 7:
    if ret == 1:
        NovoCarro()
    elif ret == 2:
        Informacoes()
    elif ret == 3:
        excluirCarro()
    elif ret == 4:
        ligarCarro()
    elif ret == 5:
        desligarCarro()
    elif ret == 6:
        ListarCarros()
    ret = Menu()
        
        
        
        
