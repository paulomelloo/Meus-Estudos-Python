texto = "O rato roeu a roupa do rei de Roma"
print(texto)

if "roupa" in texto: # se existir a palavra roupa, ira mostrar mostrar o print abaixo
    print('Encontramos a palavra \'roupa\' no texto')

if "paulo" not in texto: # se NÃO EXISTIR a palavra paulo, ira mostrar o print abaixo
    print('Não encontramos a palavra \'paulo\' no texto')

print('rei' in texto) # vai retornar True, pois TEM (IN) a palavra rei na frase
print('rei' not in texto) # vai retornar False, pois tem a palavra rei na frase, no caso usamos o NOT IN (não ter) por isso o false.
print('paulo' in texto) # vai retornar False, pois não tem essa palavra no 'texto'
print('paulo' not in texto) # vai retornar True, pois nao tem essa palavra no 'texto'.