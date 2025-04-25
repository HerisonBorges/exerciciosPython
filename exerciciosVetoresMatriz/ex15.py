vetor_1 = []
vetor_compactado = []

for i in range(5):
    numero = int(input("Digite um numero: "))
    vetor_1.append(numero)

for numero in vetor_1:
    if numero > 0:
        vetor_compactado.append(numero)
print(vetor_1)
print(vetor_compactado)