"""
Criar uma classe que modela um cachorro, definindo seus atributos básicos e uma ação simples.
Crie uma Classe chamada Cachorro.
Defina o método construtor (__init__) que recebe e inicializa dois atributos:
nome
raca
Defina um terceiro atributo interno chamado idade, inicializando-o com o valor 0.
Crie um Método chamado latir() que imprime uma mensagem simples usando o nome do cachorro (Ex: "Max diz: Au Au!").
Crie um Método chamado envelhecer() que apenas incrementa (+= 1) o atributo idade.
Fora da classe, crie dois Objetos diferentes da classe Cachorro e chame o método latir() para ambos.
"""

class Cachorro:
    def __init__(self,nome, raca):
        self.nome = nome
        self.raca = raca
        self.idade = 0

    def latir(self):
        print(f'{self.nome} late: Au Au')
    
    def envelhecer(self):
        self.idade += 7
    
dulce = Cachorro("Dulce", "pug")
print(dulce.nome)
print(dulce.raca)

dulce.latir()
dulce.envelhecer()
print(dulce.idade)
dulce.envelhecer()
print(dulce.idade)