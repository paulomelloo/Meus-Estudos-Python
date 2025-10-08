def imprimeNome(nome = "Paulo"): #deixa a variavel nome ja com algo, caso ao chamar função não coloquei o valor da variavel ela pega essa que esta setado no def
    print(f'Olá {nome}!')

imprimeNome() # ira mostrar: Olá Paulo
imprimeNome("Mariana") # ira mostrar: Olá Mariana
imprimeNome("Dulce") # ira mostrar: Olá Dulce