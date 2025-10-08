"""
Crie um loop que exibe os números digitados do usuário na tela;
o loop deve ser cancelado quando o usuario digitar 0;
"""
x = 1

while x != 0:
    x = int(input("Digite um número: "))
    if x == 0:
        break


