# não pode tem um parametro opcional antes do obrigatorio
def soma_numeros(a,b,c=10): #nesse caso o parametro obrigatorio é o que nao tem valor definido, no caso A e B, parametro opcional é o C
    print(a + b + c)

soma_numeros(1,2,3) #ira mostrar 6, a=1 b=2 e c=3 (ele substitui o valor definido na função)
soma_numeros(5,5) # ira mostrar 20, a=5 b=5 e c=10 (como não foi passado valor, ele usa o valor definido na função)

# comentar linha abaixo para rodar o programa
soma_numeros(4) # vai dar erro, pois a função precisa de 2 parametros obrigatorios, no caso so passamos 1.