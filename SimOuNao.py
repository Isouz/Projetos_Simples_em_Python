from random import randint
from time import sleep

def linha():
    return '---' * 14
    
    
opc = ['\033[32mSim\033[m', '\033[31mNão\033[m']
print(linha())
print('\033[1;41mFaça uma pergunta e responderei Sim ou Não\033[m')
while True:
    print(linha())
    pergunta = str(input('\033[36mPergunta: \033[m')).upper()
    resp = randint(0, 1)
    print(linha())
    print('\33[36mAnalisando...\033[m')
    sleep(1)
    print(opc[resp])

    while True:
        print(linha())
        continua = str(input('\033[36mMais uma pergunta? [S/N] \033[m')).upper()[0]
        if continua in 'NS':
            break
        else:
            print('\033[4;31mOpcão inválida\033[m')
    if continua == 'N':
        break
print(linha())
print('\033[36mEncerrando...\033[m')
sleep(1)