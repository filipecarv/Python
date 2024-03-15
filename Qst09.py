import tkinter as tk
from tkinter import messagebox
janela = tk.Tk()
janela.title('Mensagen!')
janela['bg'] = 'lightgray'
janela.geometry('400x300')
def informação():
    messagebox.showinfo('Informação', 'Voce foi avisado que ira morrer em 3 dias meu bom!')
def Erro():
    messagebox.showerror('Erro','Voce acabou destruindo seu computador meu bom!')
def Pergunta():
    messagebox.askquestion('Pergunta','Voce gosta de comer meu bom ?')
def Aviso():
    messagebox.showwarning('Aviso','Voce foi hackeado meu bom!')
def Sim_Não_Cancelar():
    messagebox.askyesnocancel('Pergunta','Voce gosta de jogar meu bom ?')
Bt1 = tk.Button(janela, text = 'Informação', command = informação, bg = 'lightgreen', font = 'bold')
Bt1.pack(anchor = 'center', pady = 10)
Bt2 = tk.Button(janela, text = 'Erro', command = Erro, bg = 'red', font = 'bold')
Bt2.pack(anchor = 'center')
Bt3 = tk.Button(janela, text = 'Pergunta', command = Pergunta, bg = 'lightblue', font = 'bold')
Bt3.pack(anchor = 'center', pady = 10)
Bt4 = tk.Button(janela, text = 'Aviso', command = Aviso, bg = 'yellow', font = 'bold')
Bt4.pack(anchor = 'center')
Bt5 = tk.Button(janela, text = 'Pergunta 2', command = Sim_Não_Cancelar, bg = 'blue', font = 'bold')
Bt5.pack(anchor = 'center', pady = 10)
janela.mainloop()