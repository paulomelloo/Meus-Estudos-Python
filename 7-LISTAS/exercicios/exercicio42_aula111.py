"""
Cire uma lista com números de 1 a 10;
Percorra a lista com um loop e quando encontar o elemento 4 remova-o;
exiba a lista atualizada.
"""

list = [1,2,3,4,5,6,7,8,9,10]
x=0

for numero in list:
    if numero == 4:
        del list[x]
    x = x + 1
print (list)