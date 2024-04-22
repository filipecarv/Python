from tkinter import*
from tkinter import ttk
janela = Tk()
janela.title('Primeira Interface!')
janela['bg'] = 'lightgray'
janela.geometry('400x200')
def Segunda_interface():
    janela2 = Toplevel()
    janela2.title('Segunda Interface!')
    janela2['bg'] = 'lightblue'
    janela2.geometry('400x200')
    janela.withdraw()
    texto = Label(janela2, text = 'Selecione o que voce gosta meu bom!', bg = 'lightblue', font = 'bold')
    texto.pack(anchor = 'center', pady = 10)
    def Selecionar(event):
        Label['text'] = Caixa_Seleçao.get()
    Caixa_Seleçao = ttk.Combobox(janela2, values = ['Jogar', 'Assistir Filmes/Series', 'Comer', 'Dormir'])
    Caixa_Seleçao.current(0)
    Caixa_Seleçao.bind('<<ComboboxSelected>>', Selecionar)
    Caixa_Seleçao.pack()
    label = Label(janela2, text = 'Aguardando sua resposta meu bom!', pady = 50)
    label.pack()
Bt1 = Button(janela, text = 'Proxima Interface!', command = Segunda_interface, bg = 'lightgreen')
Bt1.pack(anchor = 'center', pady = 70)
janela.mainloop()