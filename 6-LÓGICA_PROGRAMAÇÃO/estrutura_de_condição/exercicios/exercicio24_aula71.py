"""
Escreva um programa que recebe dois números
Insira a multiplicação entre eles em uma variavel
se for menor ou igual a 100 o resultado, insira uma mensage que o número é baixo e acima de 100 o número é alto
"""

num1 = float(input("Insira o primeiro número: "))
num2 = float(input("Insira o segundo número: "))

mult = num1 * num2

if mult <= 100:
    print(f"a multiplicação dos {num1} e {num2} é {mult}, número é BAIXO!")
else:
    print(f"a multiplicação do {num1} e {num2} é {mult}, o número é ALTO!")