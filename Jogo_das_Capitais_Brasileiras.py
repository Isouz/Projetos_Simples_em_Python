#Acerte capitais de cada estado
#Bibliotecas
from time import time, sleep
from random import shuffle


def linha():
    print('--'*14)

#Dicionario dos Estados e Capitais
brasil = {'Acre':'Rio Branco','Alagoas':'Maceió','Amapá':'Macapá',
'Amazonas':'Manaus','Bahia':'Salvador','Ceará':'Fortaleza',
'Espírito Santo':'Vitória','Goiás':'Goiânia','Maranhão':'São Luís',
'Mato Grosso':'Cuiabá','Mato Grosso do Sul':'Campo Grande','Minas Gerais':'Belo Horizonte',
'Pará':'Belém','Paraíba':'João Pessoa','Paraná':'Curitiba',
'Pernambuco':'Recife','Piauí':'Teresina','Rio de Janeiro':'Rio de Janeiro',
'Rio Grande do Norte':'Natal','Rio Grande do Sul':'Porto Alegre',
'Rondônia':'Porto Velho','Roraima':'Boa Vista',
'Santa Catarina':'Florianópolis','São Paulo':'São Paulo',
'Sergipe':'Aracajú','Tocantins':'Palmas'}

#Randomizando o dicionário
lista_br = list()
for k, v in brasil.items():
    lista_br.append([k,v])

shuffle(lista_br)

#Dicionario das Respostas
lista_resp = list()
for item in lista_br:
    lista_resp.append([item[0]])
print('==' * 14)

#Contagem de acertos
cont = 0

#Inicio do programa
linha()
print('Desafio das Capitais')
sleep(1)
print()
print('   Escreva o nome da capital do estado que aparecer na tela.')
print()
#sleep(5)
print('   Não se esqueça de colocar a acentuação correta.')
#sleep(5)
linha()
print()
print('Começando em...')
sleep(1)
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print('Valendo!')
temp_i = time()
linha()

#Perguntas
for est in range(len(lista_resp)):
    print(f'{lista_resp[est][0]}', end='')
    lista_resp[est].append(str(input(' = ')))
    if lista_resp[est][1] == lista_br[est][1]:
        cont += 1
linha()
linha()

#verificando as respostas
for uf in range(len(lista_resp)):
    sleep(0.4)
    print(f'Estado: {lista_resp[uf][0]}')
    if lista_br[uf][1] == lista_resp[uf][1]:
        print(f'Capital: \033[32m', end='')
        print(f'{lista_br[uf][1]}\033[m')
    else:
        print(f'Sua resposta: \033[31m', end='')
        print(f'{lista_resp[uf][1]}\033[m')
        print(f'Capital: {lista_br[uf][1]}')
    linha()

#Resultados
print('Calculando pontuação...')
temp_f = time()
temp_total = temp_f - temp_i
minutos = temp_total // 60
segundos = temp_total % 60
sleep(2)
print(f'Tempo total: {minutos:.0f}:{segundos:.0f}')
sleep(0.5)
print(f'Pontuação total: {cont}/26')
sleep(0.5)
nota = (cont / 26) * 10
print(f'Nota final: {nota:.2f}')
sleep(0.5)
linha()