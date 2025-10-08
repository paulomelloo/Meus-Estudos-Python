lista = [1,2,3,4]
print(lista)

lista.append(5)
print(lista)

n_lista = ["paulo", "mariana"]
print(n_lista)
n_lista.append("dulce") #adicionou dulce na n_list
print(n_lista)

#caso não tenha nenhum elemento com o nome 'familia' sera adicionado.
if len(n_lista) != "familia":
    n_lista.append("familia")
print(n_lista)