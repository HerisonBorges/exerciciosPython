class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir(self):
        print(self.titular, self.saldo)


minhaConta = Conta("Herison", 1000)
minhaConta.exibir()

class contaVip(Conta):
    def render(self):
        self.saldo += 100
        print("--- Rendimento VIP Aplicado ---")
        



vip = contaVip("Herison vip", 2000)
vip.exibir()
vip.render()
vip.exibir()
