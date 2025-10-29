def removerDuplicatas(lista):
    return list(set(lista))


listaDuplicatas = []

while True:
    entrada = input("Digite o numero: ")

    if entrada.lower() == 's':
        break

    else:
        num = int(entrada)
        listaDuplicatas.append(num)

print(listaDuplicatas)
novaLista = removerDuplicatas(listaDuplicatas)
print(novaLista)