frutas = ["uva", "banana", "uva", "maçã", "banana", "uva"]

contagemFrutas = {}

for chave in frutas:
    if chave in contagemFrutas:
        contagemFrutas[chave] += 1
    else:
        contagemFrutas[chave] = 1

print(contagemFrutas)