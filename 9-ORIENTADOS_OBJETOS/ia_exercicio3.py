"""
Criar uma classe para realizar cálculos geométricos, utilizando os atributos do objeto.
1- Crie uma Classe chamada Retangulo.
2- Defina o método construtor (__init__) que recebe e inicializa dois atributos:
    largura
    altura
3- Crie um Método chamado calcular_area() que retorna o valor da área (largura × altura).
4- Crie um Método chamado calcular_perimetro() que retorna o valor do perímetro (2×(largura+altura)).
5- Crie um Método chamado redimensionar(nova_largura, nova_altura) que simplesmente atualiza os atributos largura e altura do objeto.
6- Crie um Objeto Retangulo, imprima a área e o perímetro, use o método redimensionar(), e imprima a nova área e perímetro.
"""
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        area = self.largura * self.altura
        print(f'A área do retangulo é {area}')
    
    def calcular_perimetro(self):
        perimetro = 2*(self.largura + self.altura)
        print(f'O perimetro do retangulo é {perimetro}')
    
    def redimensionar(self, nova_largura, nova_altura):
        self.largura = nova_largura
        self.altura = nova_altura
        print(f'O retangulo foi dimensionado para altura {self.altura} e largura {self.largura}')

objeto1 = Retangulo(4,5)
print(f'O Retangulo possui altura {objeto1.altura} e largura {objeto1.largura}.')

objeto1.calcular_area()
objeto1.calcular_perimetro()
print('---')
objeto1.redimensionar(nova_altura=2,nova_largura=3)
objeto1.calcular_area()
objeto1.calcular_perimetro()