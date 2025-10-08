"""
Peça ao usuário para digitar três números, chamados ladoA, ladoB e ladoC.
Se ladoA for igual a ladoB E ladoB for igual a ladoC, mostre: "É um Triângulo Equilátero (três lados iguais)." 
Senão, se (elif) ladoA for igual a ladoB OU ladoA for igual a ladoC OU ladoB for igual a ladoC, mostre: "É um Triângulo Isósceles (dois lados iguais)." 
Senão (se nenhuma das condições acima for verdadeira, ou seja, todos os lados são diferentes), mostre: "É um Triângulo Escaleno (todos os lados diferentes)." 
(Dica: Em Python, o "E" é and e o "OU" é or)
"""

ladoa = int(input("Digite o valor do lado A: "))
ladob = int(input("Digite o valor do lado B: "))
ladoc = int(input("Digite o valor do lado C: "))

if ladoa == ladob and ladoa == ladoc:
    print(f"É um triangulo EQUILATERO (3 lados iguais)")
elif (ladoa == ladob and ladob != ladoc) or (ladoa != ladob and ladob == ladoc) or (ladoa == ladoc and ladoc != ladob):
    print(f"É um Triangulo Isóceles (dois lados iguais)")
else:
    print (f"É um triangulo escaleno (todos os lados diferentes)")
    