def soma(a,b): # função soma criada
    return a + b

def mult(a,b): # funcao mult criada
    return a * b

def operacao (a, b, f): # funcao operacao criada, onde F é a chamada de outra funcao
    resultado= f(a,b)
    return resultado

print(operacao(5,5,soma)) # informado parametro A=5,B=5 e F=soma (vai somar a + b)
print(operacao(2,4,mult)) # informado parametro A=2,B=4 e F=mult (vai multiplicar a + b)

