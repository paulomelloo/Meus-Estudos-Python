class Person: # criei uma classe Person sem nada, só para teste de delete mesmo
    pass

paulo = Person() # criado o Objeto paulo na classe Person
mariana = Person() # criado o objeto mariana na classe Person

print(paulo) # mostra que pertence a classe Person
print(mariana) # mostra que pertence a classe Person

del mariana # deleta o objeto mariana

print(paulo)
print(mariana) # agora vai dar erro, pois não tem como mostrar o objeto mariana deletado
# pra executar o programa vai ter que remover a linha acima.
