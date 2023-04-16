from random import randint
from time import sleep
#Funçoes


def cabeçalho(msg):
    print('--' * 14)
    print(msg)
    print('--' * 14)
    
    
def linha():
    print('--' * 14)
    
    
def invalida():
    print('\033[31mOpção Invalida. Tente novamente.\033[m')
  

#Variaveis  
resp = 'S'
  
#Menu de seleção  
linha()
print('\033[39;41m           Dados           \033[m')
while True:
    resp = 'S'
    while True:
        try:
            linha()
            print('\033[32m')
            print('Escolha o tipo de dado: ')
            print('[1] Dado de 6 lados')
            print('[2] Dado de 12 lados')
            print('[0] Sair do programa')
            escolha = int(input('Sua escolha: \033[m'))
            linha()
            if escolha > 2:
                invalida()
            else:
                break
        except:
            linha()            
            invalida()
    if escolha == 0:
        print('\033[36mEncerrando Programa...\033[m')
        sleep(1)
        cabeçalho('Obrigado. Volte sempre!')
        break
    elif escolha == 1 or escolha == 2:
        while True:
            try:
                qnt = int(input('\033[32mQuantidade de dados: \033[m')) 
                if qnt != 0:
                    break
                else:
                    linha()
                    invalida()
                    linha()
            except:
                linha()
                invalida()   
    else:
        invalida()
        
#Lançamento dos dados
    while resp != 'M':
        if escolha == 1:
            linha()
            print('\033[32mLançando dados...')
            print('\033[36m')
            sleep(1)
            for dado in range(1, qnt + 1):
                print(f'Dado n°{dado} = {randint(1, 6)}')
            print('\033[m')
            linha()             
        else:
            linha()
            print('\033[32mLançando dados...')
            print('\033[36m')
            sleep(1)
            for dado in range(1, qnt + 1):
                 print(f'Dado n°{dado} = {randint(1, 12)}')
            print('\033[m')   
            linha()    
        resp = str(input("""\033[32mLançar novamente? 
Digite qualquer valor para continuar
Ou [M] para retornar ao menu principal: \033[m""")).upper()[0]

