"""
Crie um programa com a variável salario
se for maior que 1800 imprima uma mensagem que é necessário pagar imposto de rende
Senão imprima uma mensagem que não precisa pagar
"""

sal = float(input("Digite seu Salario: "))

if sal <= 1800:
    print(f"Seu salario é R${sal}, não é necessário pagar imposto de renda!")
else:
    print(f"Seu salário é R${sal}, necessário pagar imposto de renda!")