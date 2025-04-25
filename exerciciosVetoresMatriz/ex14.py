vetor = []
vetor2 = []
vetorI = []
for i in range(10):
    numero =  int(input("Digite os numeros do primeiro vetor: "))
    vetor.append(numero)
for i in range(10):
    numero2 = int(input("Digite os numeros do segundo vetor: "))
    vetor2.append(numero2)
for numero, numero2 in zip(vetor,vetor2):
    vetorI.append((numero,numero2))
print(vetor)
print(vetor2)
print(vetorI)