class Aviao:
    __asas = 2 # privado, só pode ser acessado/modificado dentro dessa clase, no caso usamos a função mostrar_asas

    def __init__(self, marca):
        self.marca = marca
    
    def mostrar_asas(self): # funcao que utiliza o __asas (atributo privado)
        print(f'Aviao tem {self.__asas} asas')

aviao = Aviao("Aviao voar")
print(aviao.marca)
#print(aviao.__asas) # vai dar erro, pois é um ATRIBUTO PRIVADO, só pode ser usado em outra função dentro da classe
# para executar o programa, comentar o código acima
aviao.mostrar_asas()