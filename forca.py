from random import choice

temas = ['Carro', 'Comida', 'Cidade']
tema = choice(temas)
palavras_carro = ['gol', 'palio', 'uno', 'hilux']
palavras_comida = ['pizza', 'carne', 'biscoito', 'bolo']
palavras_cidade = ['florianopolis', 'Carangola']
palavras_forca = []

if tema == 'Carro':
    palavras_forca = palavras_carro
elif tema == 'Comida':
    palavras_forca = palavras_comida
elif tema == 'Cidade':
        palavras_forca = palavras_cidade

print(f'O tema é: {tema}')

palavra_forca = choice(palavras_forca)

print(f'A palavra possui {len(palavra_forca)} letras')
print('Você possui 3 tentativas para acertar a palavra')

digitadas = []
conta_chance = 3
while True:
    letra = str(input("Digite uma letra: "))
    if len(letra) > 1:
        print('Erro, não vale mais de uma letra por tentativa')
        continue
    
    digitadas.append(letra)

    palavra_secreta = ''
    for letra_secreta in palavra_forca:
        if letra_secreta in digitadas:
            palavra_secreta += letra_secreta
        else:
            palavra_secreta += '*'

    if palavra_secreta == palavra_forca:
        print('Parabéns, você venceu')
        print(f'A palavra é {palavra_forca}')
        break
    else:
        print(f'A palavra secreta está assim: {palavra_secreta}')

    if letra not in palavra_secreta:
        conta_chance -= 1
    
    if conta_chance <= 0:
        print('Você perdeu')
        break

    print(f'Você ainda tem {conta_chance} chances')
    print()

