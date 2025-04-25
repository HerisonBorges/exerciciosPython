matriz = []
pares = 0
soma_impares = 0

numLinha = int(input("Digite o numero de linhas: "))
numcolunas = int(input("Digite o numero de colunas: "))
for i in range(numLinha):
    linha_atual = []
    for j in range(numcolunas):
        elemento = int(input(f"Digite o valor para a posição ({i}, {j}): "))
        linha_atual.append(elemento)
        if elemento % 2 == 0:
            pares += 1
        else:
            soma_impares += elemento
    matriz.append(linha_atual)


for linha in matriz:
    print(linha)

total = numLinha * numcolunas 
soma_total = sum(sum(linha) for linha in matriz)
media = soma_total / total


print("A quantidade de elementos pares é:", pares)
print("A soma dos elementos ímpares é:", soma_impares)
print("A média dos elementos na matriz é:", media)