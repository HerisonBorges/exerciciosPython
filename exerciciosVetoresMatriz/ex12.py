vetor = []

for i in range(6):
    elemento = float(input("Digite o valor do elemento: "))
    vetor.append(elemento)

codigo = int(input("Ditite 0 para terminar o codigo, 1 para ordem direta e 2 para reversa: "))
    
if codigo == 0:
    print("Algoritimo terminado")
    
elif codigo == 1:
    for elemento in vetor:
        print(elemento, end=" ")
elif codigo == 2:
    for elemento in reversed(vetor):
        print(elemento)