"""
Crie uma classe Carro com as propriedades marca, valor, número de portas e tanque de gasolina;
Crie um método que abastece o taque de gasolina;
Crie um método dirigir que remove gasolina baseado em uma km rodada.
"""
class Carro:
    def __init__(self, marca, valor, tanque):
        self.marca = marca
        self.valor = valor
        self.tanque = tanque
    
    def abastece(self, litros):
        if self.tanque >= 50:
            print(f'Tanque esta cheio')
        else:
            self.tanque += litros
            if self.tanque > 50:
                self.tanque = 50

    def dirigir(self,km):
        if km >= self.tanque:
            self.tanque = 0
            print(f'Acabou o combustivel, abasteça novamente!')
            self.tanque = 0
        else:
            self.tanque = self.tanque - km
            print(f'Ainda sobrou {self.tanque} Litros!')
            

fusca = Carro("fusca", 30000, 30)
print(fusca.tanque)

fusca.abastece(100)
print(fusca.tanque)

fusca.dirigir(51)
print(fusca.tanque)