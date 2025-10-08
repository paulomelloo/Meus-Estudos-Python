def saudacao(nome): # cria a funcao(def) saudacao, com a variavel nome
    return f"Ola {nome}" # o return ele salva o resultado da função 

sds = saudacao("Paulo") # no caso o resultado da funcao saudacao foi salva na variavel 'sds'
print(sds) #ira mostrar: Ola Paulo
print(sds + ' tudo bem?') # ira mostrar: Ola Paulo tudo bem?

print('----') #outros exemplos

# divisao
def div (x, y): # crio a funcao div
    return x / y

d = div(10, 2) # criou a variavel 'd' com a divisao de 10 por 2
print(f'Divisao: {d}') # ira mostrar: 'Divisao: 5.0'

# soma
def soma (a, b): # criou a função soma
    return a + b

s = soma(2,4) #criou a variaval 's' com a soma de 2 + 4
p = soma(2,2) # criou a variavel 'p' com a soma de 2 + 2
print(s) # ira mostrar 6
print(s + p) # soma os valores das 2 variaveis 's' e 'p'. Ira mostrar: 10


def profissao(nome):
    p = "" # na verdade nao precisa dessa variavel vazia, vou deixar para simplificar a lógica
    if nome == "professor":
        p = "programador"
    else:
        p = "estudante"
    return p

prof = profissao("paulo")
print(prof)