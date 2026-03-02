class Conta:
    def __init__(self):

        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def mostrar(self):
        print(self.saldo)
    
        
c1 = Conta()
c2 = Conta()

c1.depositar(20)
c1.sacar(5)

c2.depositar(10)
c2.sacar(3)

c1.mostrar()
c2.mostrar()