import tkinter as tk
from tkinter import messagebox
def Botão():
  messagebox.showinfo('Mensagem', 'Bem vindo meu bom!')
janela = tk.Tk()
janela.title('Mensagem Misteriosa!')
janela['bg'] = 'lightgray'
janela.geometry('300x200')
Botao = tk.Button(janela, text = 'Clique aqui seu curioso!', command = Botão, bg = 'lightgreen')
Botao.pack(anchor = 'center',pady = 70)
janela.mainloop()