"""
Escreva uma função que recebe uma lista de números;
Calcule a média dos números da lista.
"""

def mediaNum(lista):
    soma = 0

    for x in lista:
        soma += x

    media = soma / len(lista)
    return media

notas = [10,9,8,7,6]
print(mediaNum(notas))

notas1000 = [1000, 930, 720, 598]
print(mediaNum(notas1000))