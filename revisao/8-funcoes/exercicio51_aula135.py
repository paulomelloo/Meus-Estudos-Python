"""
Crie uma função que retorna se um número é maior ou menor que 10;
O número deve ser passado como parâmetro.
"""

def valorNum(numero):
    resultado = ""
    if numero > 10:
        resultado = "Maior que 10"
    elif numero < 10:
        resultado = "Menor que 10"
    else:
        resultado = "Igual a 10"
    return resultado

print(valorNum(int(input('Digite o valor desejado: '))))