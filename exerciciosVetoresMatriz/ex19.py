vetor1 = []
vetorPar = []
vetorImpar = []

for i in range(8):
    numero = int(input(f"Digite o valor da posição {i}: "))
    vetor1.append(numero)
print(vetor1)

for numero in vetor1:
    if numero % 2 ==0:
        vetorPar.append(numero)
print(vetorPar)
for numero in vetor1:
    if numero % 2 !=0:
        vetorImpar.append(numero)
print(vetorImpar)