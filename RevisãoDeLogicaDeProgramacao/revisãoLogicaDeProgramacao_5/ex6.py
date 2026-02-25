class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Carrinho(Produto):
    def __init__(self):
        self.itens = []
    def adicionar(self, produto_recebido):
        self.itens.append(produto_recebido)

    def exibirCarrinho(self):
        for p in self.itens:
            print(f"Produto: {p.nome} - R$ {p.preco}")


p1 = Produto("Mouse", 50)
p2 = Produto("Teclado", 150)

meuCarrinho = Carrinho()
meuCarrinho.adicionar(p1)
meuCarrinho.adicionar(p2)

meuCarrinho.exibirCarrinho()