"""
Escreva uma função que desenha uma escada no terminal;
Os números de degruas deve ser informado por parâmetro.
"""

degraus = int(input('Digite o número de degraus: '))
simbolo = input('Digite o simbolo do degrau: ')

def escada(n):
    for x in range(degraus):
        print(simbolo * (x+1))

escada(degraus)