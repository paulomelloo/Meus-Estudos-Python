dic = {
}
#criei um dic vazio
print(dic)

dic["nome"] = "Paulo" # adicionei a chave nome com o Valor Paulo no dicionario
print(dic) # aqui vai TUDO que tem no dicionario 'dic'
print(dic["nome"]) # aqui vai mostrar somente o Valor da chave "nome" no 'dic': Paulo

del dic["nome"]
print(dic)