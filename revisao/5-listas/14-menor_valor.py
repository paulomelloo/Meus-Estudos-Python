lista = [77,42,2,39,50,99]

#exemplo com for
menor_valor = 99999

for x in lista:
    if x < menor_valor:
        menor_valor = x

print(menor_valor)

#exemplo com while
menor_valor = 99999
z = 0
while z < len(lista):
    if lista[z] < menor_valor:
        menor_valor = lista[z]
    z += 1

print(menor_valor)
