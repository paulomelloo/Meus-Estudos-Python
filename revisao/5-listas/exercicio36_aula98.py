"""
Crie uma lista com 5 notas de prova de um aluno;
faça um loop que calcula a média das notas
IMPRIMA O RESULTADO FINAL
"""

notas = [10,8,9,6,7]
i = 0
soma = 0

while i < len(notas):
    soma = soma + notas[i]
    i += 1

media = soma / len(notas)
print(media)