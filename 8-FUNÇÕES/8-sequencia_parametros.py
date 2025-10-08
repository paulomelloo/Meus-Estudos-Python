def soma_todos(*nums): # trabalha com uma lista de parametros indefinidos (não tem limite)
    soma = 0
    for x in nums: # um FOR que vai somar todos os numeros apresentados como parametros (pode ser quantos quiser, não tem limite)
        soma += x
    
    return soma

print(soma_todos(1,2,3,4,5,6,)) # vai mostrar a soma de todos os numeros, no caso 21
print(soma_todos(100, 10, 20, 70, 1)) # a soma é 201