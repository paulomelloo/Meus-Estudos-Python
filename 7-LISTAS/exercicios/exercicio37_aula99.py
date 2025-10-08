"""
Crie uma lista com 5 valores zerados;
faça um loop para percorrer a lista e preencher os valores zerados;
os valores devem ser inseridos pelo usuario;
imprima o resultando final como print
"""
lista = [0,0,0,0,0]
i=0

while i < 5:
    lista[i] = input("Digite um valor para lista: ")
    i = i + 1

print (lista)