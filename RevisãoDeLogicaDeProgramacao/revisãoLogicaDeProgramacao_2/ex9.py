estoque = []

for _ in range(6):
    valores = int(input("Digite aqui o valor: "))

    estoque.append(valores)

print(estoque)

maior = estoque[0]
menor = estoque[0]

for item in estoque:
    if item > maior:
        maior = item
    elif item < menor:
        menor = item

print(maior)
print(menor)