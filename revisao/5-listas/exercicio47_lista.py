"""
Crie uma lista com lsitas dentro dela;
Uma ideia seria: produtos com nome, cor e preço;
Imprima cada um dos itens da listas que estão inseridas na lista pai.
"""

lista1 = ["sutia", "vermelho", 25]
lista2 = ["calcinha", "preto", 20]
lista3 = ["meia calça", "branco", 35]
lista4 = ["lingerie completa", "azul marinho", 70]

listas_full = [lista1, lista2, lista3, lista4]

for x in range(len(listas_full)):
    for z in range(len(listas_full[x])):
        print(listas_full[x][z])

# metodo diferente, escrevendo cada lista em 1 linha
for y in listas_full:
    print(f'Produto {y[0]}, com a cor {y[1]} e valor R${y[2]}')