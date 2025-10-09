class Veiculo: # criação da classe Veiculo padrao
    def __init__(self, rodas, marca):
        self.rodas = rodas
        self.marca = marca

    def ligar(self):
        print('Veiculo ligado!')

class Carro(Veiculo): # Aqui criei uma Classe herança Carro, onde a classe PAI é o Veiculo
    def __init__(self, rodas, marca, teto_solar):
        super().__init__(rodas, marca) # aqui mostra que rodas e marca são da Classe PAI (Veiculo), onde os objetos são os mesmos da classe PAI (rodas, marca)
        self.teto_solar = teto_solar

ferrari = Carro(4, "Ferrari", True)

print(ferrari.marca)
ferrari.ligar()

class Moto(Veiculo):
    def __init__(self, rodas, marca, protecao_lateral):
        super().__init__(rodas, marca)
        self.protecao_lateral = protecao_lateral

    def empinar(self):
        print('Empinou a moto!')

moto = Moto(2, "honda", False)
print(moto.rodas)

moto.ligar()
moto.empinar()