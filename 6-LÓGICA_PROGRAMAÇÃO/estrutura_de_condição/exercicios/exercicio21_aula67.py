"""
Crie um programa que recebe o número de rodas que o veículo possui;
Se for mais que 2, imprima uma mensagem para pagar o pedágio;
Se foir igual a 2, imprima uma mensagem dizendo que pode passar livremente1
"""

roda = int(input("Digite o número de rodas: "))

if roda > 2:
    print(f"PAGAR O PEDÁGIO!")

if roda <= 2:
    print(f"Pode seguir viagem!")