listaCompras = []

for _ in range(3):
    produto = input("Informe o nome do produto: ").lower()

    listaCompras.append(produto)


print(listaCompras)
print(len(listaCompras))

if "ovo" in listaCompras:
    print("Cuidado ao carregar os ovos!")
else:
    print("Lista finalizada com sucesso!")