"""
Evitar ao máximo usar a CÓPIA DE LISTA LINKADA
NORMALMENTE usa a CÓPIA DE LISTA INDEPENDENTE
"""
#COPIA DE LISTA LINKADA (Se altera a pai, altera a filho tb.)
lista = [1,2,3]
nova_lista = []
nova_lista = lista
print(f"lista: {lista}")
print(f"nova lista: {nova_lista}")

lista[0]=444 # alterando o valor de 1 para 444, altera em ambas as listas
print(f"lista: {lista}")
print(f"nova lista: {nova_lista}")

#COPIA DE LISTA INDEPENDENTE (se alterar uma não afeta a outra, listas diferentes)
lista_original = [1,2,3,4,5]
lista_copia = []
lista_copia = lista_original[:]
print(f"Lista Original é: {lista_original}")
print(f"lista copia é: {lista_copia}")

lista_copia[0] = 555 # altera o valor 1 para 555 somente da lista_copia, a lista_original continua intacta

print(f"Lista Original é: {lista_original}")
print(f"lista copia é: {lista_copia}")

