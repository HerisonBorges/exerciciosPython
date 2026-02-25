class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar(self, p):
        self.itens.append(p)

    def exibir(self):
        for i in self.itens:
            print(f"{i.nome} - R$ {i.preco}")

    def calcularTotal(self):
        total = 0
        for i in self.itens:
            total += i.preco
        
    
        print(f"Total da compra: R$ {total:.2f}")

meuCarrinho = Carrinho()

while True:
    n = input("Nome do produto (ou 'sair'): ").lower()
    if n == 'sair':
        break

    val = float(input("Preço: "))
    novo = Produto(n, val)
    meuCarrinho.adicionar(novo)
        

meuCarrinho.exibir()

meuCarrinho.calcularTotal()