class Conta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibirSaldo(self):
        print(f"Saldo atual é {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso!")
        else:
            print("Saldo insuficiente!")


minhaConta = Conta("Herison", 1000)
minhaConta.depositar(500)
minhaConta.sacar(200)
minhaConta.exibirSaldo()