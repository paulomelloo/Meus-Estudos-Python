class Carro:

    rodas = 4 # é uma Atributo de classe(propriedade de classe) constante, não varia, independente da classe

    def __init__(self, marca): # aqui é a 
        self.marca = marca

fusca = Carro("fusca")

print(fusca.marca)
print(fusca.rodas)