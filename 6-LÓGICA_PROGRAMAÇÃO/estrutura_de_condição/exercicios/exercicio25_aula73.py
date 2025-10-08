"""
Escreva um programa que receba um número;
verifique se o número é maior que 10, senão imprima uma mensagem avisando que para prosseguir precisar ser maior que 10;
no primeiro if verifique se o número é menor que 20 e imprima a multiplicação dele por 2, senão imprima o número multiplaco por 5.
"""

num = int(input("Digita um número: "))

if num > 10:

    if num < 20:
        novo_num = num * 2
        print(f"O número é menor que 20, foi multiplicado por 2, novo numero é {novo_num}")
    else:
        novo_num = num * 5
        print(f"O número é maior que 20, foi multiplicado por 5, novo numero é {novo_num}")
        
else:
    print(f"O número é menor ou igual a 10, precisa ser um número maior!")