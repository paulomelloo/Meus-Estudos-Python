def soma_todos(*nums): #quando coloca * na frente, trabalha com varios parametros (não tem limite)
    soma = 0
    for x in nums:
        soma += x
    return soma

print(soma_todos(1,2,3,4))
print(soma_todos(1,2,324,5,5,34,3,5))