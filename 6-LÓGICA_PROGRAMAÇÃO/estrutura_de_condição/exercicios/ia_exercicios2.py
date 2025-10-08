"""
 Calcular o preço final de uma compra com base no valor e aplicar descontos em faixas.
 Se o valor_da_compra for maior que 500, aplique um desconto de 15% e mostre o valor final.
 Senão, se (elif) o valor_da_compra for maior que 200, aplique um desconto de 10% e mostre o valor final.
 Senão (se o valor for 200 ou menos), mostre o valor sem desconto e a mensagem: "Sem desconto aplicado."
"""

valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 500:
    print(f"Desconto de 15%")
    valor_total = valor_compra - (valor_compra * 15 / 100)
    print(f"Valor com desconto é de R${valor_total}")

elif valor_compra > 200:
    print(f"Desconto de 10%")
    valor_total = valor_compra - (valor_compra * 10 / 100)
    print(f"Valor com desconto é de R${valor_total}")

else:
    print(f"O valor da compra é R$ {valor_compra}, sem desconto aplicado!")