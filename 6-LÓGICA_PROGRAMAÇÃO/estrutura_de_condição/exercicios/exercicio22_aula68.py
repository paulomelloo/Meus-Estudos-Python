"""
Escreva um programa que lê dois números;
Depois imprima o maior deles
"""
num1 = float(input("Escreva o primeiro número: "))
num2 = float(input("Escreva o segundo número: "))

if num1 > num2:
    print(f"O número maior é {num1:.0f}")

if num1 < num2:
    print(f"O número maior é {num2:0f}")

if num1 == num2:
    print(f"Os números são iguais")