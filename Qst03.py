from tkinter import*
import tkinter as tk
janela = Tk()
janela.title('Ta ai os Pack(Side) meu bom!')
janela.geometry('400x200')
janela['bg']='lightgray'
Bt1 = Button(janela, text='Pack(Top)')
Bt1.pack(side = TOP)
Bt2 = Button(janela, text='Pack(Left)')
Bt2.pack(side = LEFT)
Bt3 = Button(janela, text='Pack(Right)')
Bt3.pack(side = RIGHT)
Bt4 = Button(janela, text='Pack(Bottom)')
Bt4.pack(side = BOTTOM)
janela.mainloop()