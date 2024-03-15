from tkinter import*
import tkinter as tk
janela = Tk()
janela.title('Ta ai os Pack(Place) meu bom!')
janela.geometry('400x200')
janela['bg']='lightgray'
Texto1 = tk.Label(janela, text='Botão1', font=('Arial', 12,), bg=janela['bg'])
Texto1.place(x=50,y=20)
Texto2 = tk.Label(janela, text='Botão2', font=('Arial', 12,), bg=janela['bg'])
Texto2.place(x=150,y=20)
Texto3 = tk.Label(janela, text='Botão3', font=('Arial', 12,), bg=janela['bg'])
Texto3.place(x=250,y=20)
Bt1 = tk.Button(janela, text='Place(x,y)', font=('Arial',12), bg='lightgreen')
Bt1.place(x=50,y=60)
Bt2 = tk.Button(janela, text='Place(x,y)', font=('Arial',12), bg='lightgreen')
Bt2.place(x=150,y=60)
Bt3 = tk.Button(janela, text='Place(x,y)', font=('Arial',12), bg='lightgreen')
Bt3.place(x=250,y=60)
janela.mainloop()