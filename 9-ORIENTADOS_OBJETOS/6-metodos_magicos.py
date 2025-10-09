class Pessoa: # classe padrao Pessoa
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self): # funcao String que ira retornar uma frase
        return f'O nome do usuario é {self.nome} e tem {self.idade} anos e é um {self.profissao}'
    
paulo = Pessoa("Paulo", 33, "programador") # coloca os dados para objeto Classe
print(paulo.__str__()) # Printa a função __str__: 'O nome do usuario é Paulo e tem 33 anos e é um programador'