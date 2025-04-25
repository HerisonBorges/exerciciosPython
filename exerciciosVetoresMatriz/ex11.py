vetor = []
for i in range(7):
    elemento = int(input(f"Digite o valor do elemento {i}: "))
    vetor.append(elemento)
    
for i in range(7): 
    if vetor[i]>0:
        print(f"o numero {vetor[i]} na posição {i}")