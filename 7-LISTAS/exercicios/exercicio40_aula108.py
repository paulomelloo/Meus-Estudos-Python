"""
Cire uma lista com 5 elementos de forma dinâmica;
ou seja, cada elemento deve ser inserido pelo usuário.
"""
list = []
i = 0

while i < 5:
    list.append(input(f"Digite o elemento: "))
    i = i + 1
print(list)