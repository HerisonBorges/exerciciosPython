matriz = []
num_linhas = int(input("Digite o numero de linhas: "))
num_colunas = int(input("Digite o numero de colunas: "))

for i in range(num_linhas):
    linha_atual = []
    for j in range(num_colunas):
        numero = int(input(f"Digite o número da posição {i}, {j}: "))
        linha_atual.append(numero)
    matriz.append(linha_atual)

somaslinhas = [sum(linha) for linha in matriz]

print("Matriz original")
for linha in matriz:
    print(linha)

print("Soma de cada linha:")
print(somaslinhas)

matrizResultante = []
for i, linha in enumerate(matriz):
    nova_linha = [numero * somaslinhas[i] for numero in linha]
    matrizResultante.append(nova_linha)

print("Matriz após multiplicar cada elemento pela soma de sua linha")
for linha in matrizResultante:
    print(linha)