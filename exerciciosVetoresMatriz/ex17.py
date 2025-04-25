vetor = []
for i in range(7):
    numero = int(input("Digite um numero: "))
    vetor.append(numero)

for i in vetor:
    if i % 2 == 0:
        print(i, end=', ')
for i in vetor:
     if i % 3 == 0:
        print(i, end=', ')
for i in vetor:
    if i % 2 == 0 and i % 3 == 0:
        print(i, end=', ')