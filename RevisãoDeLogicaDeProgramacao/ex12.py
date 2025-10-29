def inverterLista(lista):
    return lista[::-1]

listaDeNumeros = []

while True:

    entrada = input("Digite um numero, ou 's' para sair. ")

    if entrada.lower() == 's':
        break

    else:
        num = int(entrada)
        listaDeNumeros.append(num)

print(listaDeNumeros)
listaInvertida = inverterLista(listaDeNumeros)
print(listaInvertida)