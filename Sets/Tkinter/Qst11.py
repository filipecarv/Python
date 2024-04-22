from tkinter import *
janela = Tk()
janela.title('Ta ai os radiobutton meu bom!')
janela['bg'] = 'lightgray'
janela.geometry('300x250')
texto = Label(janela, text = 'Selecione o que voce gosta meu bom!', bg = 'lightblue')
texto.pack(anchor = 'center', pady = 10)
var = IntVar()
def Imprimir():
    Selecionado = 'Voce escolheu a opção:' + str(var.get())
    resposta['text'] = Selecionado
Bt1 = Radiobutton(janela, text = 'Jogar', variable = var, value = 1, bg = 'lightgreen')
Bt1.pack(anchor = 'center', pady = 10)
Bt2 = Radiobutton(janela, text = 'Comer', variable = var, value = 2, bg = 'lightgreen')
Bt2.pack(anchor = 'center', pady = 10)
Bt3 = Radiobutton(janela, text = 'Dormir', variable = var, value = 3, bg = 'lightgreen')
Bt3.pack(anchor = 'center', pady = 10)
Botao = Button(janela, text = 'Selecionar', command = Imprimir)
Botao.pack(anchor = 'center', pady = 10)
resposta = Label(janela, text = '')
resposta.pack(anchor = 'center', pady = 5)
janela.mainloop()