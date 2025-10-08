"""
Crie uma função que retorna se um número é maior ou menor que 10;
O número deve ser passado como parâmetro.
"""

def numMaior(numero):
    #validador = 
    if numero > 10:
        validador = "Numero maior que 10"
    else:
        validador = "Numero menor que 10"
    return validador

teste1 = numMaior(11)
print(teste1)
teste2 = numMaior(5)
print(teste2)