nomeProdutos = []
precoProdutos = []

while True:
    adicionar = input("Deseja adicionar um produto? (s/n) ").lower()

    if adicionar == "s":
        produto = input("Informe o nome do produto: ")
        preco = float(input("Informe o preço do produto: "))

        nomeProdutos.append(produto)
        precoProdutos.append(preco)

    if adicionar == "n":
        break

print(nomeProdutos)

if len(precoProdutos) > 0:
    print(sum(precoProdutos))
    print(max(precoProdutos))
else:
    print("Nenhum produto foi cadastrado.")
