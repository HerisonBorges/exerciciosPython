def aplicarDesconto(produto):

   produto["preco"] = produto["preco"] * 0.9


meuProduto = {}

meuProduto["nome"] = input("Digite o nome: ")
meuProduto["preco"] = float(input("Digite o preco: "))

desconto = aplicarDesconto(meuProduto)

print(meuProduto)