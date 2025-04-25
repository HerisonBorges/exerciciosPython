vetor = []
vetorNegativo = []
vetorPositivo = []
for i in range(10):
    elemento = int(input("Digite o valor do elemento: "))
    vetor.append(elemento)
    if elemento < 0:
        vetorNegativo.append(elemento)
    if elemento > 0:
        vetorPositivo.append(elemento)
print(vetor)
print(vetorPositivo)
print(vetorNegativo)