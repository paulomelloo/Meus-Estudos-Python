saque = 200
saldo = 250

if saque <= saldo:
    print(f"Você sacou R${saque} da sua conta!")
    sobra = saldo - saque
    print(f"Sobrou na sua conta R${sobra}")
else:
    print(f"Você não tem saldo suficiente para o saque!")
