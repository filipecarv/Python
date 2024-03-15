from tkinter import*
import tkinter as tk
janela = Tk()
janela.title('Ta ai a pirâmide meu bom!')
janela.geometry('300x200+550+100')
janela['bg']='lightgray'
Bt1 = Button(janela, text=1, bg='lightgray', padx=10, pady=10)
Bt1.place(x=140, y=0)
Bt2 = Button(janela, text=2, bg='lightgray', padx=10, pady=10)
Bt2.place(x=122, y=44)
Bt3 = Button(janela, text=3, bg='lightgray', padx=10, pady=10)
Bt3.place(x=158, y=44)
Bt4 = Button(janela, text=4, bg='lightgray', padx=10, pady=10)
Bt4.place(x=104, y=88)
Bt5 = Button(janela, text=5, bg='lightgray', padx=10, pady=10)
Bt5.place(x=140, y=88)
Bt6 = Button(janela, text=6, bg='lightgray', padx=10, pady=10)
Bt6.place(x=175, y=88)
janela.mainloop()