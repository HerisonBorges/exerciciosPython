class Carrinho:
    def __init__(self):
        self.produtos = []

    def adicionar(self, produtos):
        self.produtos.append(produtos)
        
    def mostrar(self):
        for p in self.produtos:
            print(p)


c1 = Carrinho()
c1.adicionar("Arroz")
c1.adicionar("Feijão")

c2 = Carrinho()
c2.adicionar("Macarrão")

c1.mostrar()
c2.mostrar()


