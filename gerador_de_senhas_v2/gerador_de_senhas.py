#Gerador de senhas
from mytools import *

     
while True:
    menu()
    opc = test('Opcão:')
    if opc == 0:
        print()
        print('\033[36mObrigado e volte sempre!\033[m')
        break
    elif opc == 1:
        while True:
            create()
            answer = repeat()
            if answer:
                pass
            else:
                break
    elif opc == 2:
        print('\033[32mDigite a quantidade de caracteres desejada\033[m')
        print()
        upe = test('Letras maiusculas: ')
        low = test('Letras minúsculas: ')
        num = test('Números: ')
        spe = test('Especiais: ')
        while True:
            create(upe, low, num, spe)
            answer = repeat()
            if answer:
                pass
            else:
                break
    else:
        print()
        print('\033[31mOpção inválida!\033[m')
        print()


#Desenvolvido por Igor Souza.
#GitHub - https://github.com/Isouz