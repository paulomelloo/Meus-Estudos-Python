"""
Escreva uma função que desenha uma escada no terminal;
Os números de degraus deve ser informado por parametro;
ex:
#
##
###
####
#####
"""

def escada(valor):
    x = 1
    while x <= valor:
        print(simbolo * x)
        x += 1

degraus = int(input('Digite o numero de degraus: '))
simbolo = input('Digite o simbolo para escada: ')

escada(degraus)
escada(10)