vetor = []
negativos = 0
soma = 0
for i in range(10):
    elemento =  int(input(f"Digite o valor do elemento {i}: "))
    vetor.append(elemento)
    if elemento < 0:
        negativos+=1
    elif elemento > 0:
        soma+=elemento
print(vetor)
print("Quantidade de numeros negativos é", negativos)
print("A soma dos numeros positivos é", soma)