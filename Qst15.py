import tkinter as tk
from tkinter import messagebox
def Média():
    N1 = float(nota1.get())
    N2 = float(nota2.get())
    Média = (N1 + N2) / 2
    messagebox.showinfo('Média', f'A média deu: {Média:.2f} meu bom!')
janela = tk.Tk()
janela.title('Média')
janela['bg'] = 'lightgray'
janela.geometry('300x200')
Nota1 = tk.Label(janela, text = 'Primeira Nota:', bg = 'lightblue')
Nota1.pack()
nota1 = tk.Entry(janela)
nota1.pack()
Nota2 = tk.Label(janela, text = 'Segunda Nota:', bg = 'lightblue')
Nota2.pack()
nota2 = tk.Entry(janela)
nota2.pack()
Caucular = tk.Button(janela, text = 'Média', command = Média, bg = 'lightgreen')
Caucular.pack()
janela.mainloop()