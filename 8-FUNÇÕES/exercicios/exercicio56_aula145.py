"""
Crie uma função que recebe outra como parâmetro;
a que vai receber parâmetros deve receber um nome, uma idade e uma profissão.
A função de argumento deve apresentar estes dados em uma string dinâmica
"""

def dinamica(nome, idade, profissao):
    return f'{nome} tem {idade} anos e é {profissao}'
    # ou pode usar as 2 linha abaixo, mesma coisa que a linha acima.
    #frase = f'{nome} tem {idade} anos e trabala com {profissao}'
    #return frase

def dados(nome,idade,profissao, f):
    mostrar = f(nome,idade,profissao)
    return mostrar

print(dados("Paulo", 33, "desempregado", dinamica))

print(dados("Mariana", 36, "fisioterapeuta", dinamica))

print(dados("Dulce", 48, "cachorra", dinamica))