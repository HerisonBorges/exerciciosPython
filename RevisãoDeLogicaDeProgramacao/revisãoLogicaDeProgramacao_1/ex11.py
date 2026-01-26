def contarElementos(lista, elemento):
    numeroElementos = lista.count(elemento)
    return numeroElementos

listaElementos = []

while True:
    entrada = input("Digite um numero inteiro ou 'sair': ")

    if entrada.lower() == 'sair':
        break

    try:
        elemento = int(entrada)
        listaElementos.append(elemento)
    except ValueError:
        print("Digite um numero, ou digite 'sair': ")

print (listaElementos)

numeroElementos = contarElementos(listaElementos, elemento)
print(numeroElementos)
