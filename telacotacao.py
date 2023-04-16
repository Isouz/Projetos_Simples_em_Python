import PySimpleGUI as sg
from cotacao import pegar_cotacoes

sg.theme('DarkAmber')

layout = [
[sg.Text('Pegar cotação de moeda')],
[sg.InputText(key='nome_cotacao')],
[sg.Button('Pegar cotação'), sg.Button('Cancelar')],
[sg.Text('', key="texto_cotacao")],
]

janela = sg.Window('Sistema de cotações', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break
    if evento == "Pegar cotação":
        codigo_cotacao = valores["nome_cotacao"]
        cotacao = pegar_cotacoes(codigo_cotacao)
        janela["texto_cotacao"].update(f'A cotação de {codigo_cotacao} é de R${cotacao}')

janela.close()