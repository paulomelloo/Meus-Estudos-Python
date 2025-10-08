"""
Crie um programa que recebe o seu nome como dade;
imprima o seu nome e uma frase de saudação utilizando a string dinâmica
"""

nome = input("Digite seu nome: ")
saudacao = "Seja bem vindo/a,"

print(saudacao + " " + nome)
print("%s %s" %(saudacao,nome))
print(f"{saudacao} {nome}")