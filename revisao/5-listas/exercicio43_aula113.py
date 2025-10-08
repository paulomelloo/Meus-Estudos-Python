"""
Crie uma lista com alguns itens;
peça dois itens ao usuario;
identifique qual foi encontrado primeiro na lista.
"""

transporte = ["carro", "moto", "bicicleta", "caminhao", "onibus", "aviao", "barco"]

item1 = input('Digite o primeiro elemento: ')
item2 = input('Digite o segundo elemento: ')

i = 0

while i < len(transporte) :
    if transporte[i] == item1:
        print(f"{transporte[i]} encontrado primeiro")
        break
    elif transporte[i] == item2:
        print(f"{transporte[i]} foi encontrado primeiro")
        break
    i += 1
