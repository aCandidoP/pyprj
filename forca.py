from random import choice

comida = ['pizza', 'carne', 'sorvete', 'biscoito']
cidade = ['betim', 'juiz de Fora', 'belem', 'rio de janeiro']
palavra = ''
letras_usuario = []
palavra_secreta = ''

ganhou = False


while True:
    try:
        escolha = int(input('Bem vindo ao jogo da forca, escolha entre tema Comida (1) ou Cidades (2) ou digite qualquer outro número para sair: '))
        
        if escolha == 1:
            palavra = choice(comida)
            break

        elif escolha == 2:
            palavra = choice(cidade)
            break

        else:
            print('SAINDO DO PROGRAMA -------')
            break
     
    except ValueError:
        print('O valor digitado não é um número inteiro válido')
        break

if escolha == 1:
    tema = 'Comida'
if escolha == 2:
    tema = 'Cidade'

print(f'o tema é {tema} e a palavra tem {len(palavra)} letras')




chances = 5

while (chances != 0) and (palavra_secreta != palavra):
    print(f'Ainda lhe restam {chances} tentativas')
    for letra in palavra:
        
        try:
            letra_escolhida = str(input('Escolha uma letra: '))
            if len(letra_escolhida) > 1:
                print('Você digitou mais de 1 letra')
                continue
            if letra_escolhida.isdigit():
                print('Você digitou um número, espero uma letra')
                continue
                
            else:
                letras_usuario.append(letra_escolhida)

        except:
            print('O dígito não é uma letra')
            continue

        for letra_secreta in palavra:
            if letra_secreta in letras_usuario:
                palavra_secreta += letra_secreta
            else:
                palavra_secreta += '*'

        if palavra_secreta == palavra:
                print('Parabéns, você venceu')
                print(f'A palavra é {palavra}')
                break
        else:
            print(f'A palavra secreta está assim: {palavra_secreta}')

        print(f'Ainda lhe restam {chances} tentativas')

        if letra_escolhida not in palavra:
                chances -= 1
    
        if chances <= 0:
                print('Você perdeu')
                break
        
        palavra_secreta = ''
            
           
        






    



