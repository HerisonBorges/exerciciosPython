vetor_1 = []
vetor_2 = []
vetor_resultado = []

for i in range(5):
    numero1 = int(input("Digite o numero para o primeiro vetor:"))
    vetor_1.append(numero1)
for i in range(5):
    numero2 = int(input("Digite o numero para o segundo vetor:"))
    vetor_2.append(numero2)

for numero1, numero2 in zip(vetor_1,vetor_2):
    vetor_resultado.append((numero1*numero2))
print(vetor_1)
print(vetor_2)
print(vetor_resultado)