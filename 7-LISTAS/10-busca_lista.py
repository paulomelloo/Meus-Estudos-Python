lista = ["sofa", "televisao", "radio", "ac", "poltrona"]
palavra = input("Procure a palavra: ")

i=0
achou = False

while i < len(lista):
    if lista[i] == palavra:
        print(f"Encontramos {palavra}")
        achou = True
    i += 1 # ou i = i + 1

if achou == False:
        print(f"Não encontramos {palavra} na lista")
    
print (lista)