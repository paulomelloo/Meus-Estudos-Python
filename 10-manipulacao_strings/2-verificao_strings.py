frase = "Testamos o inicio da string" # variavel tipo string

print(frase.startswith("Testamos")) # verificar se o COMEÇO da variavel frase é 'Testamos', no caso é correto, retorna True
print(frase.startswith("inicio")) # verifica se o COMEÇO da variavel frase é 'inicio', no caso é incorreto, retorna False

if (frase.startswith("Testamos") == True): # se a primeira palavra for 'Testamos' ira mostrar o primeiro print, senão vai mostrar o segundo.
    print('Encontramos a primeira palavra da viaravel frase')
else:
    print('Não é a primeira palavra da variavel frase')


print(frase.endswith('string')) # verifica se o FINAL da variavel frase é 'string', no caso esta correto, retorna True
print(frase.endswith('Testamos')) # verifica se o FINAL da variavel frase é 'Testamos, no caso esta incorreto, retorna False