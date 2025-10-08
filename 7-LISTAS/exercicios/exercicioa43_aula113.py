"""
Crie uma lista com alguns itens;
Peça dois itens ao usuário, identifique qual foi encontrado primeiro na lista;
"""

l = ["edicula", "churrasqueira", "piscina", "sinuca", "ac"]

achar1 = input("Digite o item 1: ")
achar2 = input("Digite o item 2: ")

i=0

while i < len(l):
    if l[i] == achar1:
        print(f"O item {achar1} foi encontrado primeiro na lista")
        break
    elif l[i] == achar2:
        print(f"O item {achar2} foi encontrado primeiro na lista")
        break
    i += 1