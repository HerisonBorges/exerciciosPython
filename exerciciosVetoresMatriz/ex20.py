vetor = []
for i in range(12):
    numero = int(input(f"Digite o numero da posição {i}:"))
    vetor.append(numero)
print(vetor)

maiorNumero = max(vetor)
print(maiorNumero)

vetorDivisão = []
for numero in vetor:
    divisão = numero / maiorNumero
    vetorDivisão.append(divisão)
print(vetorDivisão)