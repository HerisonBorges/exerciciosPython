class Lampada:
    def __init__(self):
        self.estado = "Apagada"

    def ligar(self):
        self.estado = "Acessa"

    def desligar(self):
        self.estado = "Apagada"

    def mostrar(self):
        print(self.estado)

l1 = Lampada()
l2 = Lampada()

l1.ligar()
l1.mostrar()
l2.mostrar()

l2.ligar()
l2.desligar()
l2.mostrar()