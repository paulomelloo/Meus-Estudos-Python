def soma (a, b): # funçao soma criada
    return a + b

def multiplicacao (a, b): # funcao multiplicaçao criada
    return a * b

def operacao(a, b, f): # função operação: Temos que fornecer 2 valores e uma funcao
    resultado = f(a, b) # F vai ser a funçao que vai ser chamada para tratar o valor A e B
    return resultado

print(operacao(5,5,soma)) # no caso vai usar 5+5 pois chamamos a funçao soma
print(operacao(2,4,multiplicacao)) # no caso vai usar 2*4 pois chamaos a função multiplicação