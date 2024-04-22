from tkinter import *
janela = Tk()
janela.title('Imagem!')
janela['bg'] = 'lightgray'
janela.geometry('800x450')
img = PhotoImage(file='Imagem.png')
image = Label(janela, image=img)
image.pack()
janela.mainloop()