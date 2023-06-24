from random import randint
import os


def clear():
    if os.name == 'nt':   # Limpar o terminal no Windows
        os.system('cls')
    else:                 # Limpar o terminal em sistemas Unix
        os.system('clear')


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
        'banheiro', 'bilhete', 'tenista', 'testar',]
    pos = randint(0, len(words) - 1)
    return words[pos]


def show(text):
    pal = ''
    for i in text:
        pal += f'{i} '
    print('\033[36m', pal, '\033[m')


def info(life, wrong, tried):
    body(life)
    print("" * 2, "")
    print(wrong)
    print("" * 2, "")
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


#Desenvolvido por Igor Souza.
#GitHub - https://github.com/Isouz