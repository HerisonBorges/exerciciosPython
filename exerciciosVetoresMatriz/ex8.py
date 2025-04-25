vetor = []
for i in range (7):
    elemento = int(input(f"Digite o valor do elmento {i}: "))
    vetor.append(elemento)
print(vetor)

matriz = []
linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de coluanas: "))

for i in range(linhas):
    linha=[]
    for j in range(colunas):
        elemento = int(input(f"Digite o elemento de {i+1}, {j+1}: "))
        linha.append(elemento)
    matriz.append(linha)
for linha in matriz:
    print(linha)