carro_a = ["bmw", 80]
carro_b = ["ferrari", 100]
carro_c = ["fusca", 1]

carros = [carro_a, carro_b, carro_c]
print(carros) # vai mostrar [['bmw', 80], ['ferrari', 100], ['fusca', 1]]

print(carros[0]) # vai filtrar a primeira lista(elemento) dentro da lista 'carro': ['bmw', 80]

print(carros[1][0]) # vai filtrar a segunda lista(elemento) dentro da lista carros ['ferrari', 100], depois filtra o primeiro elemento dessa sub-lista, vai mostrar: ferrari

print(carros[2][1]) # filtrei a terceira lista(elemento) dentro da lista carros ['fusca', 1], depois filtrei o segundo elemento dessa sub-lista, vai mostrar: 1

# Pegar a marca dos carros com FOR
for marca in carros:
    print(f'A marca do carro é {marca[0]}')

# Pegar o valor dos carros com WHILE
x=0
while x < len(carros):
    print(f'O valor do carro é {carros[x][1]}')
    x += 1