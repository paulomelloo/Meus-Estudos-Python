dados = {
    "nome": "Paulo",
    "sobrenome": "Mello",
    "idade": 33,
}
print(dados)

print('nome' in dados)
print('nascimento' in dados)

if 'nome' in dados:
    print(f'Nome é {dados['nome']}')