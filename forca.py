# Forca
from random import randint
from os import system
from time import sleep


def target():
    words = [
        'escada', 'fralda', 'banho', 'faca',
        'banana', 'chave', 'sapato', 'bolsa',
        'beijo', 'flores', 'bateria', 'carro',
        'colar', 'brinco', 'python', 'homem',
        'tempo', 'coisa', 'caminho', 'privada',
        'borboleta', 'abacate', 'xicara', 'prato',
        'caneca', 'senha', 'corredor', 'porta',
        'poltrona', 'ratoeira', 'resposta', 'gato',
        'tradutor', 'abismo', 'conversa', 'torre',
        'estado', 'ferramenta', 'morango', 'marrom',
        'melancia', 'ervilha', 'cavalo', 'verde',
        'laranja', 'bigode', 'diretor', 'boca',
        'cabelo', 'neto', 'quadrado', 'livro',
        'jornal', 'padeiro', 'advogado', 'patins',
        'roupa', 'telefone', 'foguete', 'arquiteto',
        'produtivo', 'amigo', 'regra', 'sapateiro',
        'perna', 'raspador', 'porta', 'esquerda',
        'banheiro', 'bilhete', 'tenista', 'testar',
    ]
    pos = randint(0, len(words) - 1)
    return words[pos]


def show(text):
    pal = ''
    for i in text:
        pal += f'{i} '
    print('\033[36m', pal, '\033[m')


def info(life, wrong, tried):
    body(life)
    print()
    print(wrong)
    print()
    show(tried)


def body(life):
    if life == 6:
        print("""
|==.==
|  .
|  .
|
|
|
|
________""")
    elif life == 5:
        print("""
|==.==
|  .
|  .
|  0
|
|
|
________""")
    elif life == 4:
        print("""
|==.==
|  .
|  .
|  0
|  |
|
|
________""")
    elif life == 3:
        print("""
|==.==
|  .
|  .
|  0
| /|
|
|
________""")
    elif life == 2:
        print("""
|==.==
|  .
|  .
|  0
| /|\\
|
|
________""")
    elif life == 1:
        print("""
|==.==
|  .
|  .
|  0
| /|\\
| /
|
________""")
    else:
        print("""
|==.==
|  .
|  .
|  0
| /|\\
| / \\
|
________""")


life = 6
word = target()
tried = ''
wrong = []

# cores do terminal
red = '\033[31m'
gre = '\033[32m'
yel = '\033[33m'
cl = '\033[m'

system('clear')

for element in word:
    tried += '_'

while True:
    info(life, wrong, tried)
    if life == 0:
        print()
        print(f'{red}Você perdeu! a palavra era {cl}{word}.')
        break
    if tried == word:
        print(gre, 'Parabens! Você venceu.', cl)
        break
    print()
    letter = str(input('Digite uma letra: ').lower().strip())

    if len(letter) > 1:
        print()
        print(yel, 'Digite uma letra por vez', cl)
        sleep(1)
        system('clear')

    elif letter in word:
        system('clear')
        for l in range(len(word)):
            if word[l] == letter:
                tried = tried[:l] + word[l] + tried[l + 1:]
            else:
                pass
    elif letter in wrong or letter in tried:
        print(yel, 'Você já digitou essa letra', cl)
        print()
        sleep(1)
        system('clear')
    else:
        system('clear')
        wrong.append(letter)
        life -= 1

# modularizacao
# docstrings
