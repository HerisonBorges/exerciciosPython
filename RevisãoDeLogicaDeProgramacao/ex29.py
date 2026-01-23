lista_produtos = []

while True:
    nome = input("Digite o nome do produto: ")
    preço = float(input("Digite o preço: "))
    
    produto = {"nome": nome, "preço": preço}
    lista_produtos.append(produto)

    sair = input("Deseja continuar? (s/n)")

    if sair == "n":
        break

for item in lista_produtos:
    print(item)