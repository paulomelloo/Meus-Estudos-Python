texto = "Esta é a frase que vamos checar as ocorrências da palavra frase"

print(texto.count("frase")) # vai retornar 2, pois foi repetido 2x a palavra 'frase' na variavel texto.

print(texto.find("frase")) # vai retornar 9, pq a partir do indice (posição) 9 que aparece a palavra 'frase'
print(texto.find("vamos")) # vai mostrar 19, pq a partir do indice (posição) 19 que aparece a palavra 'vamos'.
print(texto.find("paulo")) # vai retornar -1, pq não existe essa palavra no texto.