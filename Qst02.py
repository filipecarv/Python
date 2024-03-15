from tkinter import*
import tkinter as tk
janela = Tk()
janela.title('Informe isso dai meu bom!')
janela.geometry('400x200')
janela['bg']='lightgray'
Nome = tk.Label(janela, text='Informe seu nome meu bom!', font=('Arial', 12, 'bold'), bg=janela['bg'])
Nome.pack(anchor='center')
entry1 = tk.Entry(janela)
entry1.pack(anchor='center')
Idade = tk.Label(janela, text='Informe sua idade meu bom!', font=('Arial', 12, 'bold'), bg=janela['bg'])
Idade.pack(anchor='center')
entry2 = tk.Entry(janela)
entry2.pack(anchor='center')
button = tk.Button(janela, text='Salvar')
button.pack(anchor='center', pady=20)
janela.mainloop()