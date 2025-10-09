"""
Crie uma classe Pessoa com nome e idade;
Crie uma classe de Super Heroi que herda as características báscas de pessoa;
Crie poderes especiais para o super heroi.
Teste as duas classes criando novos objetos.
"""
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self):
        print('Ola Galera!')

class Superheroi(Pessoa):
    def __init__(self, nome, idade, poder):
        super().__init__ (nome, idade)
        self.poder = poder
    
    def superpoder(self):
        print(f'Sou um Super Heroi e meu poder é {self.poder}')
    
paulo = Pessoa("Paulo", 33)
dulce = Superheroi("Dulce", 7, "super força")

paulo.falar()
dulce.falar()
dulce.superpoder()