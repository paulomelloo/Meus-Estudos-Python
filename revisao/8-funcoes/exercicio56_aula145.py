"""
Crie uma função que recebe outra como parâmetro;
A que vai receber parâmetros deve receber um nome, uma idade e uma profissao.
A funcao de argumento deve apresentar estes dados em uma string dinamica.
"""

def apresentacao(nome,idade,prof,f):
    retorna = f(nome,idade,prof)
    return retorna

def dados(nome,idade,prof):
    return f'Meu nome é {nome}, tenho {idade} anos e sou {prof}'

def futuro(nome,idade,prof):
    return f'{nome}, no futuro com {idade} anos que estar trabalhando como {prof}'

print(apresentacao("paulo", 33, "analista de infra",dados))
print(apresentacao("mariana", 36, "fisiterapeuta", dados))

print(apresentacao("paulo", 34, "programador", futuro))
print(apresentacao("mariana", 37, "empresaria", futuro))