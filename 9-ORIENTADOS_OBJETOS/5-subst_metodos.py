class Pessoa:
    def falar(self):
        print('Ola Pessoal!')

class Paulo(Pessoa):
    def falar(self):
        print('Ola, meu nome é Paulo Mello') # aqui substituimos a função falar. Se alguem pertencer a classe Paulo, ira usar essa função falar e não a da Classe Pessoa.
    #pass # não declarar nada nessa Classe
    
paulo = Paulo()
mariana = Pessoa()

paulo.falar() # ira mostrar a função falar da classe Paulo: Ola, meu nome é Paulo Mello.
mariana.falar() # ira mostrar 'Ola Pessoal!', pois mariana não pertence a Classe Paulo e então não ira usar a função falar dessa classe.

# lembre que função é igual a MÉTODO para Classes