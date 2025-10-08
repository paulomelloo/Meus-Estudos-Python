lista = [1,2,3]
nova_lista = []

nova_lista = lista # a 'nova_lista' é uma copia vinculada da 'lista'

print(f'lista original {lista}')
print(f'lista clone {nova_lista}')

nova_lista[0] = 1000 # alterei o elmeneto 0 da 'nova_lista'.
print(f'lista original {lista}')
print(f'lista clone {nova_lista}')
#desse modo acima, estamos fazendo um CLONE da lista (então se eu modificar tanto a lista_nova quanto a lista, ambas vão sofrer alteração)

print('--------------')

numeros = [0,1,2,3,4]
novo_numeros = []

novo_numeros = numeros[:] # a lista 'novo_numeros' é uma copia desvinculada da lista 'numeros'.

print(f'lista numeros(original): {numeros}')
print(f'lista novo_numeros(copia): {novo_numeros}')

novo_numeros[0] = 1000 # alterei o elemento 0 da lista 'novo_numeros'.

print(f'lista numeros(original): {numeros}')
print(f'lista novo_numeros(copia): {novo_numeros}')
#desse modo acima, estamos fazendo um COPIA da lista numeros desvinculada (então se eu modificar a novo_numeros não ira modificar a numeros) SÃO TABELAS DIFERENTES.

