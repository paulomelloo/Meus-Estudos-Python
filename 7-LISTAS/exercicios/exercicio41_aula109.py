"""
Cire duas variaveis de listas;
crie uma terceira lista com todos os elementos das duas listas anteriores.
"""

lista_a = [1,2,3,4,5]
lista_b = [6,7,8,9,10]
#lita_c = lista_a[:] + litas_b[:]
#print(c)
# OU

lista_c = []
i = 0
j = 0

while i < len(lista_a):
    lista_c.append(lista_a[i])
    i = i + 1
while j < len(lista_b):
    lista_c.append(lista_b[j])
    j = j + 1
print(lista_c)
