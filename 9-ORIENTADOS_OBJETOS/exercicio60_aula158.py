"""
Crie uma classe Carro com as propriedades de portas, motor, se tem teto solar, marca, preço.
Crie objetos preenchendo os valores das propriedades.
"""

class Carro:
    def __init__(self, portas, motor, tetoSolar, marca, preco):
        self.portas = portas
        self.motor = motor
        self.tetoSolar = tetoSolar
        self.marca = marca
        self.preco = preco

bmw = Carro(4, 4.0, True, "bmw", 350000)

print(f'Portas: {bmw.portas}')
print(f'Motor: {bmw.motor}')
print(f'Teto Solar: {bmw.tetoSolar}')
print(f'Marca: {bmw.marca}')
print(f'Preco: R${bmw.preco}')
