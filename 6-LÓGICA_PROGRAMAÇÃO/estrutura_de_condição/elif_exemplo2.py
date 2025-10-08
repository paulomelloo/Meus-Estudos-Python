num = int(input("Digite um número de 1 a 19: "))

if num > 0 and num < 5:
    print(f"Maior que 0")
elif num > 5 and num < 10:
    print(f"Maior que 5")
elif num > 10 and num < 15:
    print(f"Maior que 10")
elif num > 15 and num < 20:
    print(f"Maior que 15")
else:
    print("Número não esta entre 1 e 19")