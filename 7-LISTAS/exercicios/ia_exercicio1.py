"""
Exercício 2: Somando Elementos de uma Lista (for)
Objetivo: Usar o loop for para percorrer uma lista de números e calcular a soma total.
Lista: Crie uma lista chamada numeros com os seguintes valores: [10, 5, 20, 15, 30].
Inicialização: Crie uma variável soma_total e inicialize-a com 0.
Repetição: Use um loop for para iterar diretamente sobre cada elemento da lista numeros.
Ação: Dentro do loop, adicione o valor do elemento atual à soma_total.
Resultado: Após o loop, imprima o valor final de soma_total.
"""
numeros = [10,5,20,15,30]
soma_total = 0
i = 0

while i < 5:
    soma_total = soma_total + numeros[i]
    i = i + 1

print(f"soma total é {soma_total}")