"""
estoque = [
    ["Coca", "preto", 15.00],
    ["Fanta", "laranja", 10.00],
    ["Sprite", "transparente", 12.00],
    ["Guaraná", "marrom", 13.00]
]
Inicialização: Crie as variáveis maior_preco (comece em 0) e nome_mais_caro (comece com uma string vazia).
Repetição: Use um loop for para percorrer o estoque.
Condição: Dentro do loop, use um if para verificar se o preço do produto atual (índice [2]) é maior que o maior_preco atual.
Atualização: Se for maior, atualize:
maior_preco com o novo valor.
nome_mais_caro com o nome do produto (índice [0]).
Resultado: Após o loop, imprima o nome do produto mais caro e seu preço.
"""
estoque = [
    ["Coca", "preto", 15.00],
    ["Fanta", "laranja", 10.00],
    ["Sprite", "transparente", 12.00],
    ["Guaraná", "marrom", 13.00]
]

maior_preco = 0
nome_caro = ""

for produtos in estoque:
    nome = produtos[0]
    preco = produtos[2]
    if preco > maior_preco:
        maior_preco = preco
        nome_caro = nome

print(f"O produto mais caro é {nome_caro} e preço {maior_preco}")