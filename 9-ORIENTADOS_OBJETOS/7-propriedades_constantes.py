class Carro:

    rodas = 4

    def __init__(self, marca):
        self.marca = marca

fusca = Carro("fusca")

print(fusca.marca)
print(fusca.rodas)