"""
Escreva uma função que receba uma lista de números;
Calcule a média dos números da lista.
"""

def mediaNum(numeros):
    nova_lista = []
    soma = 0
    for x in numeros:
        soma += x
    media = soma / len(numeros)
    return media

def situacao(status):
    result = ""
    if  media_final >= 7:
        result = "Aprovado"
    elif media_final >= 4:
        result = 'Recuperação'
    else:
        result = 'Reprovado'
    return result

#cria a lista com as notas
elemento = int(input('Digite a quantidade de provas realizadas: '))
lista = []
for z in range(elemento):
    num = int(input(f'Digite a nota do aluno na prova {z+1}: '))
    lista.append(num)

# chama as funções mediaNum e situacao
media_final = mediaNum(lista)
print(f'Sua média é {media_final}')

status_final = situacao(media_final)
print(f'Voce esta {status_final}')
