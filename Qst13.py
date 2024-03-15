from tkinter import*
from tkinter import ttk
janela = Tk()
janela.title('Caregamento!')
janela['bg'] = 'lightgray'
janela.geometry('400x150')
def Carregando():
    if barra['value'] < 100:
        barra['value'] = barra['value'] + 10
        porcentagem['text'] = str(barra['value']) + '%'
    else:
        porcentagem['text'] = 'Carregamento finalizado meu bom!'
porcentagem = Label(janela, text = '0%', bg = 'lightgreen')
porcentagem.pack()
barra = ttk.Progressbar(janela, length = 300)
barra['value'] = 0
barra.pack()
botao = Button(janela, text = 'Avançar', command = Carregando, bg = 'lightblue')
botao.pack()
janela.mainloop()