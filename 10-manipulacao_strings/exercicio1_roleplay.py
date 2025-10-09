"""
Recebe uma Tabela de notas.
Faz a media e depois separas os impares dos pares.
"""

notas = [10,9,8,7,6,]
soma = 0

for x in notas:
    soma += x

media = soma / len(notas)
print(f'A média das notas é {media}')

lista_pares = [[y for y in notas if y % 2 == 0]] # metodo novo de usar o for
lista_imp = [[y for y in notas if y % 2 != 0]] # metodo novo de usar o for

#for y in notas: # metodo antigo de usar o for
#    if y % 2 == 0:
#        lista_pares.append(y)
#    else:
#        lista_imp.append(y)

print(lista_imp)
print(lista_pares)
