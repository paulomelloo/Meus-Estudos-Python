"""
CRIE UM PROGRAMA QUE RECEBA O VALOR INTEIRO, QUE SERA CONSIDERADO DINHEIRO
IMPRIMA NA TELA O NÚMERO DE CÉDULAS ENTREGUES AO USUARIO
EX: pediu 60 reias, recebeu nota de 50 e outra de 10
notas diposniveis, 100, 50 20, 10
entregue notad de maior valor para menor
"""

valor_int = int(input('Digite o valor da compra: '))
valor_recebido = int(input('Digite o total pago: '))

troco = valor_recebido - valor_int
print(f'O troco sera de R${troco}')

nota_100 = 0
nota_50 = 0
nota_20 = 0
nota_10 = 0

while troco > 0 :
    if troco >= 100 :
        #print(f'Uma nota de 100')
        nota_100 += 1
        troco = troco - 100
    elif troco >= 50 and troco < 100 :
        nota_50 += 1 
        #print(f'Uma nota de 50')
        troco = troco - 50
    elif troco >= 20 and troco < 50 :
        #print(f'Uma nota de 20')
        nota_20 += 1
        troco = troco - 20
    else:
        #print(f'Uma nota de 10')   
        nota_10 += 1
        troco = troco - 10

print(f'Troco é {nota_100} notas de 100, {nota_50} nota de 50, {nota_20} notas de 20 e {nota_10} notas de 10')