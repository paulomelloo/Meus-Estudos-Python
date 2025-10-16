from tkinter import *

janela = Tk()
janela.title("GUI para projetos Python")

texto_orientacao = Label(janela, text = "Clique no botão para iniciar o programa")
texto_orientacao.grid(column=0, row=0)

texto_orientacao2 = Label(janela, text = "Clique aqui")
texto_orientacao2.grid(column=0, row=1)

janela.mainloop()