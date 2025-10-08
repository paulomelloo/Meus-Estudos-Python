"""
Crie um programa que recebe o saldo de uma conta bancaria com R$359,56
Depois insira uma nova quantia por meio de input e remova um valor de R$125,98 referente a fatura do cartão de crédito.
Imprima o valor final da conta após as operações com string dinamica
"""

saldo = 359.56
deposito = float(input("Insira o valor depositado: "))
cartao = 125.98

total = saldo+deposito-cartao

print(f"Saldo anterior era de R${saldo} \
      Foi depositado na conta R${deposito} \
      Feito o pagamento do cartao no valor de R${cartao}. Seu novo saldo é de R${total:.2f}")