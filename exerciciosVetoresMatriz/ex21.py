matriz = []
contador = 0

linhas = int(input("Digite a quantidade de linhas: "))
colunas = int(input("Digite a quantidade de colunanas: "))

for i in range(linhas):
    linhaAtual=[]
    for j in range(colunas):
        elemento = int(input(f"Digite a posição de {i} e {j} "))
        linhaAtual.append(elemento)
        if elemento >=25 and elemento <= 40:
            contador +=1
    matriz.append(linhaAtual)
for linhas in matriz:
    print(linhas)
print(f"Quantidade de elementos entre 25 e 40 é de {contador}")