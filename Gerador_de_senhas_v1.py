#Gerador de senhas Versão 1.0
from random import *

mai = chr(randint(65, 90))
min = chr(randint(97, 122))
num = chr(randint(48, 57))
num2 = chr(randint(48, 57))
spe = chr(randint(33, 47))
word = ''

for letter in range(0, 4):
    word += chr(randint(97, 122))

password = [mai, min, num, num2, spe, word]
shuffle(password)

for element in range(0, len(password)):
    print(password[element], end='')

#Desenvolvido por Igor Souza - GitHub: Isouz