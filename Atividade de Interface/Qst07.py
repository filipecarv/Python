from tkinter import*
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
    Var1 = IntVar()
    Marcar1 = Checkbutton(janela2, text = 'Jogar', variable = Var1, bg = 'lightgreen')
    Marcar1.pack(anchor = 'center', pady = 10)
    Var2 = IntVar()
    Marcar2 = Checkbutton(janela2, text = 'Assistir series/filmes', variable = Var2, bg = 'lightgreen')
    Marcar2.pack(anchor = 'center', pady = 10)
    def Selecionar():
        if Var1.get() == 1:
            resposta1['text'] = 'Primeira Opção Selecionada'
        else:
            resposta1['text'] = ''
        if Var2.get() == 1:
            resposta2['text'] = 'Segunda Opção Selecionada'
        else:
            resposta2['text'] = ''
    Bt2 = Button(janela2, text = 'Selecionar', command = Selecionar, bg = 'lightgreen')
    Bt2.pack(anchor = 'center', pady = 10)
    resposta1 = Label(janela2, text = '', bg = 'lightgreen')
    resposta1.pack()
    resposta2 = Label(janela2, text = '', bg = 'lightgreen')
    resposta2.pack()
Bt1 = Button(janela, text = 'Proxima Interface!', command = Segunda_interface, bg = 'lightgreen')
Bt1.pack(anchor = 'center', pady = 70)
janela.mainloop()