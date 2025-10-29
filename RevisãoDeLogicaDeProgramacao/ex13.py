def filtrarPares(lista):
    pares = []
    for numeros in lista:
        if numeros % 2 == 0:
            pares.append(numeros)
    return pares   


lista = []
while True:
    entrada = input("Digite um numero ou 'sair' para sair: ")

    if entrada.lower() == 'sair':
        break
    
    else:
        num = int(entrada)
        lista.append(num)

print(lista)
listaPares = filtrarPares(lista)
print(listaPares)