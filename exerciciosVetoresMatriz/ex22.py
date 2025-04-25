matriz = []

linha = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))
for i in range(linha):
    linhaAtual = []
    for j in range(colunas):
        elemento = int(input(f"Digite o valor de {i} e {j}: "))
        linhaAtual.append(elemento)
    matriz.append(linhaAtual)
for linha in matriz:
    print(linha)

maiorElemento = max(max(linha) for linha in matriz)
print(maiorElemento)

matrizMult=[]
for linha in matriz:
    novaLinha =  [elemento * maiorElemento for elemento in linha]
    matrizMult.append(novaLinha)
for linha in matrizMult:
    print(linha)