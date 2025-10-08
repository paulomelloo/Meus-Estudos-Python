"""
Escreva uma função que recebe uma lista de números;
A funçao deve retornar apenas os números pares da lista.
"""

def numPar(numero):
    nova_lista = []
    for x in numero:
        if x % 2 == 0:
            nova_lista.append(x)
    return nova_lista

#selecionar quantidade de elementos na lista e os numeros
elementos = int(input('Digite a quantidade de elementos da lista: '))
lista = []
z=0

while z < elementos:
    num_list = int(input("digite o numero desejado: "))
    lista.append(num_list)
    z += 1

print(numPar(lista))

###### ou 
def numPar2(num):
    for y in num:
        if y % 2 == 0:
            print(y)

numPar2(lista)