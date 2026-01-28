class Conta:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibirSaldo(self):
        print(f"Saldo atual é {self.saldo}")

    def depositar(self, valor):
        self.saldo += valor

minhaConta = Conta("Herison", 1000)
minhaConta.depositar(500)
minhaConta.exibirSaldo()