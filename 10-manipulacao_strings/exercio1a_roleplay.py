"""
Recebe uma Tabela de notas.
Faça uma funçao que calcule a media e depois funçoes que calculem numeros impares e numeros pares.
"""

notas = [10,9,8,7,6,]

def mediaNotas(numeros):
    soma = 0
    for x in notas:
        soma += x
    media = soma / len(notas)
    return media

def notasPar(numeros_par):
    lista_pares = [[y for y in notas if y % 2 == 0]] #metodo novo de usar o for
#    lista_pares = [] # metodo antigo de usar o for
#    for y in notas:
#        if y % 2 == 0:
#            lista_pares.append(y)
    return lista_pares

def notasImpares(numeros_impar):
    lista_impares = [y for y in notas if y % 2 != 0] # metodo novo de usar o for
#    for z in notas: # metodo antigo de usar o for
#        if z % 2 != 0:
#            lista_impares.append(z)
    return lista_impares

print(mediaNotas(notas))

print(notasPar(notas))
print(notasImpares(notas))
