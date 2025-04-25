matriz = [[],[],[]]
lista = []
for i in range(3):
    soma = 0
    for j in range(4):
        numero = int(input(f"Insira um numero inteiro na linha {i} coluna {j}\n"))
        matriz[i].append(numero)
        soma += numero
    lista.append(soma)

matriz_2 = [[],[],[]]

for i in range(3):
    for elemento in matriz[i]:
        mult = elemento * lista[i]
        matriz_2[i].append(mult)
        
for i in matriz_2:
    print(i)