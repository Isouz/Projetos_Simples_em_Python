from random import randint
from time import sleep


def linha():
    print('\033[36m--\033[m' * 18)
    
    
resp = ''
esc = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
print()
print('\033[1;46mExecute os shapes nas escalas indicadas.\033[m')
linha()
while True:
    shape = randint(1, 5)
    casa = randint(0, 11)
    print()
    print(f'\033[36mEscala:\033[m{esc[casa]}')
    print(f'\033[36mShape: \033[m{shape}')
    print()
    linha()
    resp = str(input("""\033[36mPressione qualquer tecla para continuar
Ou [S] p/ sair: \033[m""")).upper()[0]
    linha()
    if resp == 'S':
        break
print('\033[36mEncerrando...\033[m')
sleep(1)