"""
Crie uma lista com alguns itens;
Peça dois itens ao usuário, identifique qual foi encontrado primeiro na lista;
"""
from tkinter import *

l = ["edicula", "churrasqueira", "piscina", "sinuca", "ac"]


def encontrar():
    achar1 = input("Digite o item 1: ")
    achar2 = input("Digite o item 2: ")

    i=0
    while i < len(l):
        achou = ""
        if l[i] == achar1:
            achou = achar1
            return achou
            break
        elif l[i] == achar2:
            achou = achar2
            return achou
            break
        i += 1
        texto_resultado[achou]

janela = Tk()
janela.title("GUI para projetos Python")

texto_orientacao = Label(janela, text = "Clique no botão para iniciar o programa")
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text="Programa", command=encontrar)
botao.grid(column=0, row=3)

texto_resultado = Label(janela, text='')
texto_resultado.grid(column=0, row=4)
janela.mainloop()