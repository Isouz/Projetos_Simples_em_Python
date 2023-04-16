# imports
from tkinter import *

# funcões
def contar():
    ig = ignore.get()
    texto = str(campo.get('1.0', END).strip())
    qnt_palavras = len(texto.split())
    apenas = apenas_entry.get()
    qnt_apenas = 0
    if len(ig) > 0:
        textoe = texto.replace(ig, '')
        qnt_palavras = len(textoe.split())
    else:
        textoe = texto

    if len(apenas) > 0:
        qnt_apenas = textoe.count(apenas)

    qnt_texto = (len(textoe))

    res_label['text'] = f'Quantidade de caracteres: {qnt_texto}.'
    palavras_label['text'] = f'Quantidade de palavras: {qnt_palavras}.'
    apenas_label['text'] = f'Quantidade "Apenas": {qnt_apenas}.'


def limpar():
    campo.delete('1.0', END)


#Tela
janela = Tk()
janela.title('Contador de caracteres')

#Label de descrição
desc = Label(text='Digite o texto abaixo:')
desc.grid(column=0, row=0, stick='nswe', pady=20, columnspan=2)

#Campo de texto
campo = Text(height=12, width=40)
campo.grid(column=0, row=1, stick='nswe', padx=15, pady=15, columnspan=2)

#Entrada "Ignore"
ig_Label = Label(text='Ignorar: ')
ig_Label.grid(column=0, row=4, pady=10)

ignore = Entry(font=('Arial', 9))
ignore.grid(column=1, row=4, pady=10)

#Entrada "Apenas"
apenas_Label = Label(text='Apenas: ')
apenas_Label.grid(column=0, row=5, pady=10)

apenas_entry = Entry(font=('Arial', 9))
apenas_entry.grid(column=1, row=5, pady=10)

#Botões
bt_contar = Button(text='Contar', command=contar, bg='green', fg='white')
bt_contar.grid(column=0, row=6, padx=15, pady=15)

bt_limpar = Button(text='Limpar', command=limpar, bg='orange', fg='black')
bt_limpar.grid(column=1, row=6)

#Respostas
res_label = Label(text='')
res_label.grid(column=0, row=7, padx=10, pady=15, columnspan=2)

palavras_label = Label(text='')
palavras_label.grid(column=0, row=8, padx=10, pady=15, columnspan=2)

apenas_label = Label(text='')
apenas_label.grid(column=0, row=9, padx=10, pady=15, columnspan=2)

#Looping principal da Janela
janela.mainloop()

#Programado no app Pydroid 3
#Programa testado em celular com sistema Android, resolução 720 x 1280 pixel.
#Criado por Isouz - https://github.com/Isouz