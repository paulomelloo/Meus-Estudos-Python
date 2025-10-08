"""
Crie um programa que verifique o menor valor de uma lista;
"""

lista = [10,45,64,340,8,56,43,88,77]
menor_valor = 999

for x in lista:
    if x < menor_valor:
        menor_valor = x
    
print(menor_valor)