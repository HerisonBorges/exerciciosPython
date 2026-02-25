class Conta:
    def __init__(self):
        self.saldo = 0

    def depositar(self, x):
        if x > 0 :
            self.saldo += x
    
    def sacar(self, x):
        if self.saldo >= x:
            self.saldo -= x
    
    def mostrar(self):
        print(self.saldo)


c1 = Conta()
c2 = Conta()

c1.depositar(50)
c1.sacar(20)

c2.depositar(10)
c2.sacar(15)
c2.depositar(5)

c1.mostrar()
c2.mostrar()

        