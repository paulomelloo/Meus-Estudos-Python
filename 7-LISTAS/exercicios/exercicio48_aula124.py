"""
Crie um dicionario com livros que você gosta e o número de páginas;
Imprima estes valores no terminal
"""

livros = {
    "O senhor dos aneis": 532,
    "Ablon": 633,
    "O exterminio": 323,
}

for livro in livros:
    print(f"O livro {livro} tem {livros[livro]} páginas!")