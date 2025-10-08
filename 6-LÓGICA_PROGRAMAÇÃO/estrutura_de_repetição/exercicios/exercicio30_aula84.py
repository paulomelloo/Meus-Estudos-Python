"""
Crie um loop while em que o fim é determinado pelo número que o usuário insere no sistema;
Imprima os números com print.
"""

fim = int(input("Insira um número: "))
inicio = 0

while inicio <= fim:
    print(inicio)
    inicio = inicio + 1

print("fim do programa!")