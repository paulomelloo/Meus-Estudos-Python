"""
Crie um dicionario chamado carro com os seguintes valores:
pneus: 4; portas: 2; motor:1 e janelas:4
Adicione a chave teto solar com valor 1
Delete motor e janelas, imprima o dicionário novamente
"""
carro = {
    'pneu':4,
    'porta':2,
    'motor':1,
    'janela':4
}

print(carro)

carro['teto solar'] = True
del carro['motor'], carro['janela']
print(carro)