from tkinter import*
janela = Tk()
janela.title('Ta ai o espaçamento interno meu bom!')
janela.geometry('400x400+300+50')
janela['bg']='lightgray'
Bt1 = Button(janela, text='Espaçamento Interno', font = 'bold', bg='lightgrey',width= 30, height= 40)
Bt1.pack(padx=(10,10), pady=(120,120))
janela.mainloop()