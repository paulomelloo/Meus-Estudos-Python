"""
CONVERSÃO INT
"""
#metodo antigo
numero_int = input ("digite o número inteiro: ")
print(f"O número digitado é {numero_int} e é do tipo {type(numero_int)}") #ira mostrar o número e o tipo dele
print(type(numero_int)) #aqui tambem mostra o tipo da variavel

numero_int = int(numero_int) #transformamos a variavel numero para int
print(f"feito a conversao do tipo da variavel e agora o tipo da variavel é {type(numero_int)}") #ira mostrar o tipo da variavel depois da conversao

#método pratico
numero_pratico = int(input("digite o número inteiro método novo (menos linha): "))
print(f"O número digita é {numero_pratico} e o tipo da variavel é {type(numero_pratico)}")

"""
CONVERSAO FLOAT
"""
#metodo antigo
numero_float = input("digite um número float: ")
print(type(numero_float))

numero_float = float(numero_float)
print(type(numero_float)) # vai mostrar o tipo da variavel (float)
print(numero_float) #aqui vai mostrar o valor da variável

#metodo novo
numero_float_pratico = float(input("digite o número: "))
print(type(numero_float_pratico))