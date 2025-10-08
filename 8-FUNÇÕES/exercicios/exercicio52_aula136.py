"""
Escreva uma FUNÇÃO que recebe um dado em texto;
Se esse dado for mais que 20 caractere, retorna "o texto é grande" senão 'o texto é curto'
"""

def tamTexto(texto):
    validador = ""
    if len(texto) > 20:
        validador = "Texto é grande"
    else:
        validador = "texto é pequeno"
    return validador

teste1 = tamTexto("verificar se esse texto é grande")
print(teste1)

teste2 = "texto digitado"
print(tamTexto(teste2) )