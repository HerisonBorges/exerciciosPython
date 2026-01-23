precos = []

for _ in range(4):
    precosPROD = float(input("Digite aqui o preço: "))

    precos.append(precosPROD)

print(precos)

for i in range(len(precos)):
    precos[i] = precos[i] * 1.1


print(precos)