imagem = [
    [0, 255, 256, 68],
    [0, 255, 256, 68],
    [0, 255, 256, 68]
]




matriz = []

houveplantação = []
semPlantacao = []
indeterminado = []


linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))

for x in range(linhas):
    linha_atual = []
    for y in range(colunas):
        elemento = int(input(f"Digite o valor do elemento {x} {y}: "))
        linha_atual.append(elemento)
    matriz.append(linha_atual)


for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        valorPixel = matriz[x][y]

        if valorPixel > 120:
            houveplantação.append((x,y))
        elif valorPixel < 30:
            semPlantacao.append((x,y))
        else:
            indeterminado.append((x,y))

print("houve plantação:", houveplantação)
print("nao houve plantação:", semPlantacao)
print("não é possível determinar:", indeterminado)