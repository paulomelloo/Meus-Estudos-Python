"""
Crie um sistema que simule um banco, a classe deve ter um método de saque, depósito e transferência;
Propriedades nome de proprietário da conta, saldo e quais mais precisar.
Realizar saques, depósitos e tranferências dentre contas.
"""
class Banco:
    def __init__(self, proprietario, saldo, limite):
        self.proprietario = proprietario
        self.saldo = saldo
        self.limite = limite
    
    def deposito(self):
        valor_deposito = int(input('Digite o Valor que deseja depositar: '))
        self.saldo += valor_deposito
        print(f'Seu novo saldo é de {self.saldo}')
    
    def saque(self):
        valor_saque = int(input('Digite o valor que deseja sacar: '))
        if valor_saque < (self.saldo + self.limite):
            self.saldo -= valor_saque
            print(f'Seu novo saldo é de {self.saldo}')
        else:
            print('Você não possui SALDO e ja atingiu seu Limite. Não foi possível sacar!')
    
    def transferencia(self):
        valor_transf = int(input('Digite o valor que deseja tranferir:'))
        if valor_transf < (self.saldo + self.limite):
            self.saldo -= valor_transf
            print(f'Seu novo saldo é de {self.saldo}')
        else:
            print('Você não possui SALDO e ja atingiu seu Limite. Não foi possível transferir! ')
            print(f'Seu saldo é de {self.saldo}')

conta1 = Banco("Paulo Mello", 1000, 800)
print(conta1.saldo)

conta1.deposito()
conta1.transferencia()
conta1.saque()