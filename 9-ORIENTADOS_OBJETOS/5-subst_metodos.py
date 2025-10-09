class Pessoa:
    def falar(self):
        print('Ola Pessoal!')

class Paulo(Pessoa):
    def falar(self):
        print('Ola, meu nome é Paulo Mello')
    #pass # não declarar nada nessa Classe
    
paulo = Paulo()
mariana = Pessoa()

paulo.falar()
mariana.falar()