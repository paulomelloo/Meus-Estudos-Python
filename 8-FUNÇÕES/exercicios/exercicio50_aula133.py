"""
Crie uma função que exibe a multiplicação de dois números;
Os números devem ser passados por parâmetros
"""

def mult(num1, num2):
    print(num1 * num2)

num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))

mult(num1, num2) # aqui vai setar a variavel num1 e num2 e a função mult vai multiplicar os 2 números
mult(5, num2) # aqui é um teste que da pra fazer, ao inves de multiplicar as variaveis, vc pode por numero qualquer tb