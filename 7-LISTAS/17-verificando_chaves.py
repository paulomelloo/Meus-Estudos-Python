dicionario = {
    "testando": 2,
    "nome": "paulo",
    "idade": 33
}

print (dicionario)
print("nome" in dicionario)
#print("sobrenome" in dicionario)

if "nome" in dicionario:
    print(f"O seu nome é {dicionario["nome"]}")
    
if "sobrenome" in dicionario:
    print(f"O seu sobrenome é {dicionario["sobrenome"]}")