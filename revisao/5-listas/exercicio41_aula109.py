"""
Crie duas variáveis de listas;
crie uma terceira lista com todos os elementos das duas listas anteriores
"""

lista = [1,2,3,4,5]
lista2 = [6,7,8,9,10]
lista3 = []

i=0
x=0

while i < len(lista) :
    lista3.append(lista[i])
    i += 1
while x < len(lista2) :
    lista3.append(lista2[x])
    x += 1

print(lista3)