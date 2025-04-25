matriz = []
linhas = int(input("Digite o número de linhas da primeira matriz: "))
colunas = int(input("Digite o número de colunas da primeira matriz: "))
for i in range(linhas):
    linha_atual = []
    for j in range(colunas):
        elemento = int(input(f"Digite o número para a posição ({i},{j}): "))
        linha_atual.append(elemento)
    matriz.append(linha_atual)

print("\nPrimeira matriz:")
for linha in matriz:
    print(linha)

linhas2 = int(input("Digite o número de linhas da segunda matriz: "))
colunas2 = int(input("Digite o número de colunas da segunda matriz: "))
matriz2 = []

for i in range(linhas2):
    linha_atual2 = []
    for j in range(colunas2):
        elemento = int(input(f"Digite o número para a posição ({i},{j}): "))
        linha_atual2.append(elemento)
    matriz2.append(linha_atual2)

print("\nSegunda matriz:")
for linha in matriz2:
    print(linha)

# Verificando se a multiplicação é possível
if colunas != linhas2:
    print("Erro: O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
else:
    matriz_resultado = [[0] * colunas2 for _ in range(linhas)]

    
    for i in range(linhas):
        for j in range(colunas2):
            for k in range(colunas):  # Ou k em range(linhas2) (que é igual a colunas)
                matriz_resultado[i][j] += matriz[i][k] * matriz2[k][j]

    # Exibindo a matriz resultante
    print("\nMatriz resultante da multiplicação:")
    for linha in matriz_resultado:
        print(linha)