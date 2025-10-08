carro_a = ["bmw", 200000]
carro_b = ["ferrari", 400000]
carro_c = ["fusca", 15000]

carros = [carro_a, carro_b, carro_c]

print(carros) # vai mostrar a lista 'carros' com as 3 listas dentro
print(carros[0]) # vai mostrar a lista '0' (carro_a) [bmw, 200000]
print(carros[0][0]) # vai mostrar na lista (carro_a) só o primeiro elemento da primeira lista [bmw]
print(carros[2][1]) # vai mostrar na lista '2'(carro_c) só o elemento '1' [15000]

for carro in carros:
    print(f"A marca do carro é {carro[0]}")

for preco in carros:
    print(f"O preço do carr é {preco[1]}")