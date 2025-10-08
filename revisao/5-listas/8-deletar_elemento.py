lista = [10,20,30,40]
print(lista) # [10, 20, 30, 40]

del lista[0] # deletando o elemento 0 da lista
print(lista) # [20, 30, 40]

del lista[len(lista) - 1] #deletando o ultimo elemento da lista, len(lista) para mostrar a quantidade de elemento - 1 para deletar somente o ultimo
print(lista) # [20, 30]