vetor = []

for i in range(5):
    elemento = int(input(f"Digite um numero na posição {i}: "))
    vetor.append(elemento)
print(vetor)

for i in range(len(vetor)):
    if vetor[i]==10:
        print(f"numero: {vetor[i]}, na posição{i}")