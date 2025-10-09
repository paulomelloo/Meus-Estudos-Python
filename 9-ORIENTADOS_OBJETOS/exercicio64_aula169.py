"""
Crie uma classe Mamifero com propriedade de mamíferos;
Herde os detalhes desta classe e crie novas para Cachorro, Gato e Outra qualquer.
Crie objetos destas classes quer herdam de Mamifero.
Exiba as propriedades e métodos na tela.
"""
class Mamiferos:
    def __init__(self, raca, patas, rabo):
        self.raca = raca
        self.patas = patas
        self.rabo = rabo
    
class Cachorros(Mamiferos):
    def __init__(self, raca, patas, rabo, onomatopeia):
        super().__init__(raca, patas, rabo)
        self.onomatopeia = onomatopeia

class Gatos(Mamiferos,):
    def __init__(self, raca, patas, rabo):
        super().__init__(raca,patas,rabo)
    
    def miar(self):
        print('Miauu')

dulce = Cachorros("Pug", 4, True, "au au")
print(dulce.onomatopeia)

felina = Gatos("Persa", 4, True)
felina.miar()