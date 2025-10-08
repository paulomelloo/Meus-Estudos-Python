class Carro:
    def __init__(self, modelo, preco):
        self.modelo = modelo
        self.preco = preco

    def ligarCarro(self): # método criado (ligar carro) sem variavel
        print('Carro ligado, tem gasolina!')
    
    def novoPreco(self, novo_preco): # metodo criado novoPreco, com variavel novo_preco. Alterar o preço do carro
        self.preco = novo_preco

fusca = Carro("fusca", 30000)
print(fusca.modelo)
print(fusca.preco)

fusca.novoPreco(25000)

print(fusca.preco)