"""
Crie uma função que recebe uma sequência de parâmetros numéricos;
Multiplique todos eles e exiba o valor no terminal.
"""

def multiplicacao(*valores):
    mult=1 # aqui tem que ser 1 e não 0, pq multiplicar por 0 vai ser sempre 0.
    for x in valores:
        mult *= x
    return mult

print(multiplicacao(1,2,4,6))