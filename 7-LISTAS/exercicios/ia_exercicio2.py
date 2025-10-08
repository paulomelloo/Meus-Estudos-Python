"""
Exercício 3: Filtrando Nomes com Loop e Condição (for e if)
Objetivo: Percorrer uma lista de nomes e imprimir apenas aqueles que começam com a letra 'A'.
Lista: Crie uma lista chamada nomes com pelo menos 5 nomes (alguns começando com 'A' e outros não), por exemplo: ["Ana", "Bruno", "Alice", "Carlos", "Amanda"].
Repetição: Use um loop for para iterar sobre a lista nomes.
Condição: Dentro do loop, use uma estrutura if para verificar se o nome atual começa com a letra 'A'. (Dica: em Python, para acessar a primeira letra, use nome[0]).
Ação: Se a condição for verdadeira, imprima o nome.
"""

nome = ["Ana", "Bruno", "Alice", "Carlos", "Amanda"]

for prim in nome:
    if prim[0] == "a" or prim[0] == "A":
        print(prim)
