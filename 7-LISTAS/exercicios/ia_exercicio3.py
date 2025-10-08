"""
Exercício 8: Contagem de Caracteres (for em strings)
Objetivo: Percorrer uma string e contar quantas vezes uma determinada letra aparece.
Entrada: Defina uma string (ex: frase = "programacao em python"). Defina a letra a ser buscada (ex: letra_alvo = 'a').
Inicialização: Crie uma variável contador_letras e inicialize-a com 0.
Repetição: Use um loop for para iterar diretamente sobre cada caractere na frase.
Condição: Dentro do loop, use um if para verificar se o caractere atual é igual à letra_alvo.
Ação: Se for igual, incremente o contador_letras em 1.
Resultado: Imprima o total de vezes que a letra apareceu.
"""

frase = "programação em python"
letra = input("Digite a letra para ser contada: ")
x = 0

for carac in frase:
    if carac == letra:
        x = x + 1
print(x)