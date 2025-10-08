class Pessoa: # class Pessoa
    def __init__(self, nome, idade, profissao): # objetos nome, idade e profissão, (selfie só uma exigencia do python vai por mas não conta ele)
        self.nome = nome # propriedade nome (sempre tem o self)
        self.idade = idade # propriedade idade (sempre tem o self)
        self.profissao = profissao # propriedade profissao (sempre tem o self)

paulo = Pessoa("Paulo", 33, "analista") # instanciando o OBJETO, variavel 'paulo' vai ter: nome Paulo, idade 33 e profissao analista
print(paulo) # não funciona igual a linguagem imperativa

#a variavel para uso serao essas
print(paulo.nome) # objeto.propriedade, no caso vai mostrar: Paulo
print(paulo.idade) # objeto.propriedade, no caso vai mostrar: 33
print(paulo.profissao) # objeto.propriedade, no caso vai mostrar: analista

if paulo.nome != "Osmair": # usando em alguma função simples
    print(f'O nome {paulo.nome} é diferente de Osmair')

nome = paulo.nome
print(nome)