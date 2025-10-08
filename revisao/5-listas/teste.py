"""
Crie uma lista com alguns itens;
peça dois itens ao usuario;
identifique qual foi encontrado primeiro na lista.
"""

lista = ["casa", "carro", "viagem", "aviao", "praia"]

item1 = input("Digite o primeiro item: ")
item2 = input("digite o segundo item: ")

for x in range(len(lista)):
    if lista[x] == item1:
        print('Item1 foi encontrado primeiro')
        break
    elif lista[x] == item2:
        print('Item2 foi encontrado primeiro')
        break
    else:
        print('Nao foi encontrado nenhum item digitado')