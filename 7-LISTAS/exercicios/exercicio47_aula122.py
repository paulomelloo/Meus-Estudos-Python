"""
Crie uma lista com listas dentros;
Produtos com nome, cor e preço
Imprima cada um dos itens da lista que estão inseridas na lista pai.
"""

produto1 = ["coca", "preto", 15]
produto2 = ["fanta", "laranja", 10]
produto3 = ["sprite", "transparente", 12]
produto4 = ["guarana", "marrom", 13]

produtos = [produto1, produto2, produto3, produto4]

print("-- LISTA DE PRODUTOS --")

for todos_produtos in produtos:
    nome = todos_produtos[0]
    cor = todos_produtos[1]
    preco = todos_produtos[2]

    print(f"O nome do produto é {nome}, a cor é {cor} e o preço é R${preco}")
