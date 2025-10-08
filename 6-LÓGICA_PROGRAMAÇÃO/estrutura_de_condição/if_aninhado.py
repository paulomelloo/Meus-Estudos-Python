# é um IF dentro de outro IF (IF ANINHADO)

idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você pode entrar na balada!")
    pagamento = input("O método de pagamento é cartao (sim ou nao): ")
    if pagamento == "sim":
        print("Vá para a fila 2!")
    else:
        print("vá para a fila 1!")
else:
    print("você não tem idade para entra na balada!")