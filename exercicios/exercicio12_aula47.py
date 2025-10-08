"""
Crie tres variaveis (poupança, juros fatura_cartao)
Depois exiba os tres valores na mesma string utilizando a forma dinamica como se fosse a msensagem de um app de banco;
"""

poupanca=859.64
juros=3
fatura_cartao=1132.49

print("você possui R$%.2f na conta poupança, sua fatura do cartão é R$%.2f, caso não pague o juros mensal é de %.2f" %(poupanca,fatura_cartao,juros))

print(f"você possui R${poupanca:.2f} na conta poupança, sua fatura do cartão é R${fatura_cartao:.2f}, caso não pague o juros mensal é de {juros:.2f}%")
#método mais atual e utilizado de se usar