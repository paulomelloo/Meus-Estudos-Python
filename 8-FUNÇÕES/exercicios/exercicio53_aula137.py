"""
Escreva uma função que recebe uma lista de números;
a função deve retornar apenas os números pares da lista
"""

def numPar(numeros):
    validador = [x for x in numeros if x % 2 == 0] # for metodo novo
    #for x in numeros: ###### for metodo antigo
    #    if x % 2 == 0:
    #        validador.append(x)
    return validador

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
lista2 = [1234,1232,3121,687967,43456,34545]

teste1 = numPar(lista)
print(teste1)

print(numPar(lista2))