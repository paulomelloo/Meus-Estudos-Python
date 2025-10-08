teste = "palavra"
print(teste[0:2]) #retornar o INDICE 1 até 2 "pa"

frase = "Hoje esta fazendo sol aqui em São Paulo"
print(frase[18:21]) #retornar o indice 18 até 21 "sol"

tempo = frase[18:21] #vai criar a variável 'sol' que criamos atraves de um filtro da variavel frase
print(tempo) #imprimi o valor da variavel tempo 'sol'
print(f"temos um dia de {tempo} hoje!")

print (teste[:4]) #vai retornar o INDICE do 0 até 4 'pala'
print (teste[2:]) #vai retornar o INDICE DO 2 até o final 'lavra'.
print(teste[:-3]) #vai retornar o INDICE retirando os 3 ultimos do final 'pala'
print(teste[-3:]) #vai retornar o INDICE do 3º ao ultimo caractere