# Forca
from tools import *
from time import sleep

# cores do terminal
red = '\033[31m'
gre = '\033[32m'
yel = '\033[33m'
cl = '\033[m'

# Variáveis
life = 6
word = target()
tried = ''
wrong = []

clear()

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
        clear()

    elif letter in word:
        clear()
        for l in range(len(word)):
            if word[l] == letter:
                tried = tried[:l] + word[l] + tried[l + 1:]
            else:
                pass
    elif letter in wrong or letter in tried:
        print(yel, 'Você já digitou essa letra', cl)
        print()
        sleep(1)
        clear()
    else:
        clear()
        wrong.append(letter)
        life -= 1


#Desenvolvido por Igor Souza.
#GitHub - https://github.com/Isouz