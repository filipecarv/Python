from tkinter import*
janela = Tk()
janela.title('Ta ai os Pack(Fill e Side) meu bom!')
janela.geometry('500x200+500+50')
janela['bg']='lightgray'
Bt1 = Button(janela, text='PACK(FILL X - BOTTOM)', bg='lightgreen')
Bt1.pack(side = BOTTOM, fill = BOTH)
Bt2 = Button(janela, text='PACK(FILL Y - LEFT)', bg='lightgreen')
Bt2.pack(side = LEFT, fill = BOTH)
Bt3 = Button(janela, text='PACK(FILL Y - RIGTH)', bg='lightgreen')
Bt3.pack(side = RIGHT, fill = BOTH)
Bt4 = Button(janela, text='PACK(FILL X)', bg='lightgreen')
Bt4.pack(side = TOP, fill = BOTH)
janela.mainloop()