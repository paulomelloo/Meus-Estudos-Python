"""
Crie uma lista com 5 valores zerados.
faça um loop para percorrer a lista e preencher os valores zerados
Os valores devem ser inseridos pelo usuário
Imprima o resultado final com print
"""

lista = [0,0,0,0,0]
i = 0

while i < 5 :
    lista[i] = int(input('Insira um valor: '))
    i += 1

print(lista)