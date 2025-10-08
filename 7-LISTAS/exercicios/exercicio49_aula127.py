"""
CRIE UM DICIONARIO CHAMADO CARRO COM OS SEGUINTES VALORES:
pneus: 4,
portas: 2,
motor: 1,
janelas: 4,
Adicione a chave teto solar com valor 1 (true);
Delete motor e janelas, IMPRIMA o dicionário novamente
"""

dic = {
    "pneu": 4,
    "portas": 2,
    "motor": 1,
    "janelas": 4,
}

print(dic)

# adicionando teto solar
dic["teto solar"] = 1
print(dic)

# removendo motor e janelas
del dic["motor"]
del dic["janelas"]
print(dic)