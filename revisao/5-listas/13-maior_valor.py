lista = [13, 55, 8, 15, 66, 1, 92, 88]

# exemplo com FOR
maior_valor = 0

for x in lista:
    if x > maior_valor:
        maior_valor = x

print(maior_valor)

# exemplo com WHILE
maior_valor2 = 0
z = 0
while z < len(lista):
    if lista[z] > maior_valor2:
        maior_valor2 = lista[z]
    z += 1

print(maior_valor2)