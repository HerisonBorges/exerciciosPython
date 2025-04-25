matriz = []
somaPares = 0
somaImpares = 0
linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))
for i in range(linhas):
    linhaAtual = []
    for j  in range(colunas):
        elemento = int(input(f"Digite o numero {i} {j}: "))
        linhaAtual.append(elemento)
        if elemento % 2 == 0:
            somaPares += elemento
        else:
            somaImpares += elemento
    matriz.append(linhaAtual)
for linha in matriz:
    print(linha)

print(somaPares)
print(somaImpares)