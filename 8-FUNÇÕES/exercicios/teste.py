def tamanho(letra):
    if letra > 20:
        l = "Texto grande"
    else:
        l = "texto pequeno"
    return l

texto = input("Digite seu texto: ")

retorno = tamanho(len(texto))
print(retorno)