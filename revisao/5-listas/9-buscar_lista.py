l = ["sofa", "televisao","cama", "computador"]

i = 0
procura = input("O que deseja procurar: ")
achou = False

while i < len(l) :
    if l[i] == procura :
        print(f'O elemento  {l[i]} foi encontrado')
        achou = True
    i += 1

if achou == False :
    print(f'Não foi encontrado o elemento {procura}')