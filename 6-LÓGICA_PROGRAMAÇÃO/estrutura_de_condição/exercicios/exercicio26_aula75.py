"""
Crie um programa que receba a categoria, em valor númerico, de um produto:
se for 1 é uma bolsa
se for 2 é um tenis
se for 3 é uma mochila
Senão for nenhum desses, categoria não encontrada.
"""

num = int(input("Digite uma categoria (1 a 3):"))

if num == 1:
    print(f"É uma bolsa!")
elif num == 2:
    print(f"É um tenis!")
elif num == 3:
    print(f"É uma mochila!")
else:
    print(f"Categoria não foi encontrada!")