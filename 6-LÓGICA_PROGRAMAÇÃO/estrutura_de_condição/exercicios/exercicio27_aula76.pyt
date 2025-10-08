"""
Crie um programa que recebe a renda do usuário
Baseado na renda ele vai liberar um limite para o cartao de credito:
se for menos de 2000, libera 1000 de limite;
se for menor que 4000, libera 2000 de limite;
se for menor que 10000, libera 3000 de limite;
se for maior que 10000, falar com o gerente
"""

renda = float(input("Escreva sua renda mensal: "))

if renda < 2000 and renda > 0:
    print(f"Cartão de crédito no limite de R$1000")
elif renda < 4000:
    print(f"Cartão de crédito no limite de R$2000")
elif renda < 10000:
    print(f"Cartão de crédito no limite de R$3000")
elif renda >= 10000:
    print(f"Falar com o gerente do banco!")
else:
    print(f"Você não tem limite no cartão de crédito!")