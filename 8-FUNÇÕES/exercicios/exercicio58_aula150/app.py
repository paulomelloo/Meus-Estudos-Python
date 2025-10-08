"""
Crie um módulo que faz operações matemáticas como: soma, subtração, divisão e multiplicação;
Importe o módulo em outro arquivo e use suas funções.
"""
import funcoes_operacoes
try: # aprendizado novo, nao aprendida, só usei para teste
    valor1 = int(input('Digite o primeiro valor: '))
    valor2 = int(input('Digite o segundo valor: '))

    print(funcoes_operacoes.soma(valor1, valor2))
    print(funcoes_operacoes.subt(valor1, valor2))
    print(funcoes_operacoes.mult(valor1, valor2))
    print(funcoes_operacoes.divi(valor1, valor2))

except ValueError: # faz parte do aprendizado novo
    print('Por favor, insira apenas números inteiros válidos')
