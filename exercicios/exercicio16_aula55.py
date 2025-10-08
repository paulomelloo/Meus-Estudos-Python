"""
Faça um programa recebe um valor como salário e outro valor como porcentagem de aumento;
Exibça o valor total após o aumento no interpretador
"""

sal= float(input("Digite o salário: "))
porc= float(input("Digite a porcentagem do aumento: "))

aumento =sal + (sal * (porc/100))
print(f"você recebeu um aumento de {porc}% e seu salário agora é de {aumento:.2f}")