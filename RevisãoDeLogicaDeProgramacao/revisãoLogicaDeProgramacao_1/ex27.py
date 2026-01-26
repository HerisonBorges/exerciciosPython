listaCompras = []

while True:
    item = input("Digite o produto (ou 'sair'): ")
    if item == "sair":
        break

    listaCompras.append(item)

print(listaCompras)


