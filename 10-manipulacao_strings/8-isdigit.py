numero = "72"
print(type(numero)) # vai mostrar que o numero é tipo string

print(numero.isdigit()) # retorna True, pois a variavel string é composta somente por numero.

if numero.isdigit() == True: # se a variavel numero (que é string) for composta só por número, ira transformala em int
    numero = int(numero) # alterado a variavel para int

print(type(numero)) # ira mostrar que o numero é tipo int