def soma_ate_100(n):
    if n < 100:
        n += 1
        print(n)
        return soma_ate_100(n)
    else:
        return n

numero=(int(input('Digite um número: ')))
print(soma_ate_100(numero))