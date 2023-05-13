#Minhas ferramentas
from random import *
from time import sleep


def menu():
    """
    ->Exibe o menu principal.
    """
    print()
    print('\033[32m-=' * 15)
    print('MENU'.center(30))
    print('-=' * 15)
    print('Digite o número da opção')
    print()
    print('[0] Sair do programa.')
    print('[1] Gerar senha (padrão).')
    print('[2] Gerar senha personalizada.')
    print('---' * 10, '\033[m')
    
    
def create(upe=1, low=4, num=2, spe=1):
    """
    ->Função para gerar a senha.
     :param upe: quantidade de letras maiusculas.
     :param low: quantidade de letras minúsculas.
     :param num: quantidade de numeros (0 a 9).
     :param spe: quantidade de caracteres especiais.
     :returns: Retorna uma senha.
    """
    temp = []
    password = ''
    
    for element in range(0, upe):
        temp.append(chr(randint(65, 90)))
        
    for element in range(0, low):
        temp.append(chr(randint(97, 122)))
        
    for element in range(0, num):
        temp.append(chr(randint(48, 57)))
        
    for element in range(0, spe):
        temp.append(chr(randint(33, 47)))
        	
    shuffle(temp)
        	
    for element in range(0, len(temp)):
        password += temp[element]
    
    print('\033[32mGerando senha...')
    sleep(1.2)
    print()
    print(f'Senha gerada:\033[m {password}')
    print()
          

def test(msg):
    """ 
    -> Testa se reaposta do usuário é válida (um número inteiro).
    :param msg: mensagem que será exibida na solicitação da opção.
    :returns: escolha do usuário.
    """
    while True:
        try:
            num = int(input(msg))
        except:
            print()
            print('\033[31mDigite um número inteiro\033[m')
            print()
        else:
            print()
            return num
            print()
    
    
def repeat():
    """
    -> Teste de repetição. 
    :returns: Verdadeiro para repetir ou 
    Falso para retornar ao menu principal.
    """
    while True:
        opc = test('\033[32mDeseja repetir? \n[1] Sim \n[2] Não \n\033[mOpção: ')
        if opc == 1:
            return True
        if opc == 2:
            return False
        else:
            print('\033[31mOpção inválida!\033[m')
            print()
        

#Desenvolvido por Igor Souza.
#GitHub - https://github.com/Isouz