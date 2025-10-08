"""
Crie um programa que imprime todos os números pares de 1 a 50
"""

x = 0

while x <= 50 :
    if x % 2 == 0:
        print(x)
    x += 1

# aqui foi um exemplo de numero divisivel por 10, não pediu no exercicio
y = int(input('Digite um número: '))
if y % 10 == 0 :
	print(f'{y} é divisivel por 10')