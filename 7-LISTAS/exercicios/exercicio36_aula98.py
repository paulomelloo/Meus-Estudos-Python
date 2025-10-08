"""
Cria uma lista com 5 notas de prova de um aluno;
faça um loop que calcula a média das notas;
imprima o resultado final;
"""

notas = [10,9,7,8,10]
i = 0
total = 0

while i < 5:
    print(notas[i])
    total = total + notas[i]
    i = i + 1

media = total / 5
print (f"a media do aluno é {media}")