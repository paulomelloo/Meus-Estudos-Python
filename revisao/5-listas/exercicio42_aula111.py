"""
Crie uma lista com números de 1 a 10; Percorra a lista com um loop; Quando encontrar o elemento 4, remova-o
exiba a nova lista
"""

l = [1,2,3,4,5,6,7,8,9,10]
i=0
excluir = int(input(f"Digite o elemento que quer excluir (0 a 9): "))

while i < len(l) :
    if l[i] == l[excluir]:
        del l[i]
    i += 1

print(l)