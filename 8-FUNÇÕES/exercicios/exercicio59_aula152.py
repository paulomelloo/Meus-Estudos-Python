"""
Crie um programa que gera um número de 1 a 10;
peça para o usuario adivinhar o número;
E identifique se ele acertou ou não.
"""
import random
numero_random = random.randint(1,10)
#print(numero_random)

x=0
while x != numero_random:
    x = int(input('Tente adivinhar o número random de 1 a 10: '))
    if x == numero_random:
        print(f'Você acertou o número random {numero_random}')
    else:
        print(f'Você errou, tente novamente!')
