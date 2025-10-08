"""
crie uma lista com 5 elementos de forma dinamica
ou seja, cada elemento deve ser inserido pelo usuario
"""

lista = []
i = 0

while i < 5 :
    lista.append(input('Digite o valor do elemento: '))
    i += 1

print(lista)