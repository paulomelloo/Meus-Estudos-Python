"""
Crie um programa que busca por um elemento (UTILIZAR O FOR);
Imprima a mensagem com o elemento encontrado
"""

lista = [0,1,2,3,4,5,6,7,8,9,10]
procura = int(input("Digite o numero que procura: "))
achou = False

for n in lista:
    if lista[n] == procura:
        print(f"Elemento {procura} foi encontrado")
        achou = True
        break

if achou == False:
    print(f"O elemento {procura} não foi encontrado na lista!")