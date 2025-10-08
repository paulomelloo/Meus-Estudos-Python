"""
Crie uma string dinâmica exibindo o seu nome e a sua idade
Crie uma outra stirng dinâmica exibindo uma qtdade de dinheiro que você possui (precisa por os centavos, utilizar float)
"""

nome = "paulo"
idade = 32
dinheiro = 100.53

print("Meu nome é %s e tenho %d anos" %(nome, idade))
print("tenho um total de R$%.2f no banco!" % dinheiro )

print(f'Meu nome é {nome} tenho {idade} anos e estou com {dinheiro:.2f} reais no banco!')