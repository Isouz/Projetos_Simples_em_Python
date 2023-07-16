#Campeão Paladins
from random import randint
from time import sleep


def linha():
    print('\033[1;34m---\033[m' * 14)


def cabeçalho(msg):
    linha()
    print(msg)
    linha()
    
  
def invalida():
    linha()
    print('\033[1;31mOpção Inválida. Tente novamente.\033[m')
 
    
def sorteia():
    linha()
    sleep(0.5)
    print('\033[32mSorteando...')
    print('\033[m')
    sleep(1)
    
    
def num(selec):
    global n
    if selec == 1 or selec == 4:
        n = randint(0, 12) 
    if selec == 2:
        n = randint(0, 10)
    if selec == 3:
        n = randint(0, 16)
    return n
    
    
nome_classe = ['Tank', 'Suporte', 'Dano', 'Flanco']
tank = ['Ash', 'Atlas', 'Azaan', 'Barik', 'Fernando', 'Inara', 'Khan', 'Makoa', 'Raum', 'Ruckus', 'Torvald', 'Terminus', 'Yagorath']#13
suporte = ['Corvus', 'Furia', 'Grohk', 'Grover', 'Io', 'Jenos', "Mal'Damba", 'Pip', 'Rei', 'Seris', 'Ying']#11
dano = ['Betty', 'Bomb King', 'Cassie', 'Dredge', 'Drogoz', 'Imani', 'Kinessa', 'Lian', 'Octavia', 'Saati', 'Sha Lin', 'Strix', 'Tiberius', 'Tyra', 'Viktor', 'Vivian', 'Willo']#17
flanco = ['Androxus', 'Buck', 'Evie', 'Koga', 'Lex', 'Maeve', 'Moji', 'Skye', 'Talus', 'VII', 'Vatu', 'Vora', 'Zhin']#13
classes = [tank, suporte, dano, flanco]

#Inicio

linha()
print('\033[1;44m  Sorteio de Campeões Paladins  \033[m'.center(50))

#Menu
while True:
    try:
        linha()
        print('\033[1;32m- Menu principal -')
        print('\033[m')
        opcao = int(input("""\033[32mSelecione a opção que deseja sortear:
[1] Sortear apenas uma Classe.
[2] Sortear um campeão por Classe.
[3] Sortear apenas um Campeão.
[0] Sair do Programa.
- Sua opção: \033[m"""))

        #Sortear Classe
        if opcao == 1:
            n = randint(0, 3)
            sorteia()
            print(f'\033[32mClasse sorteada: \033[m{nome_classe[n]}')

        #Sortear Campeão de uma Classe
        elif opcao == 2:
            while True:
                try:
                    linha()
                    selec = int(input("""\033[32mSelecione a classe:
[1] Tank
[2] Suporte
[3] Dano
[4] Flanco
Classe: \033[m"""))
                    if selec > 4:
                        invalida()
                    else:
                        n = num(selec)
                        sorteia()
                        print(f'\033[32mCampeão {nome_classe[selec - 1]} sorteado: \033[m{classes[selec - 1][n]}')
                        break
                except:
                    linha()
                    print('\033[1;31mDigite um número inteiro\033[m')
    
        #Sortear Qualquer Campeão
        elif opcao == 3:
            sorteia()
            selec = randint(1, 4)
            n = num(selec)
            print(f'\033[32mCampeão {nome_classe[selec - 1]} sorteado: \033[m{classes[selec - 1][n]}')
        
        #Sair   
        elif opcao == 0:
            linha()
            print('\033[33mEncerrando Programa...\033[m')
            sleep(1)
            break
        else:
            invalida()
    except:
        linha()
        print('\033[1;31mDigite um número inteiro\033[m')
 

#Desenvolvido por Igor Souza.
#GitHub - https://github.com/Isouz