"""
Crie um programa que buscar por um elemento;
o método de loop é o FOR;
imprima a mensagem com o elemento encontrado.
"""

lista = [1,2,3,4,5,6,7,8,9,10]

encontre = int(input("Digite o valor para ser encontrado (1 a 10): "))

### maneira com range
for x in range(len(lista)):
    if lista[x] == encontre:
        print(f'Foi encontrado o elemento {lista[x]}')

### maneira sem range
for z in lista:
    if z == encontre:
        print(f'Foi encontrado o elemento {z}')