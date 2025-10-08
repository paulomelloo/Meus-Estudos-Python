"""
Crie uma função que recebe uma sequencia de parametros numericos;
multiplique todos eles e exiba o valor no terminal.
"""

def multTodos(*num):
    mult = 1 # tem que por o 1, pq senão vai começar multiplicando por 0 e sempre vai ser resultado 0
    for x in num:
        mult *= x
    return mult

print(multTodos(1,2,3,4))