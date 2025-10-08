"""
Escreva uma função que recebe um dado em texto;
se esse dado tem mais de 20 caracteres, retorne que é um texto longo;
Se tem menos, terone que é um texto curto.
"""

def tamTexto(frase):
    resultado = ""
    if len(frase) > 20:
        resultado = "Texto longo"
    else:
        resultado = "texto curto"
    return resultado

print(tamTexto(input('Digite sua frase: ')))