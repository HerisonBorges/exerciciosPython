def encontrarSegundoMaior(numeros):
    unicos = list(set(numeros))

    if len(unicos) < 2:
        return "Lista muito pequena"
    else:
        ordenados = sorted(unicos)
    return ordenados [-2]

listaExemplo = [1,2,3,4,4,4,5,6,6]

resultado = encontrarSegundoMaior(listaExemplo)

print(listaExemplo)
print(resultado)

listaPequena = [1,1,1]

resultadoPequeno = encontrarSegundoMaior(listaPequena)

print(listaPequena)
print(resultadoPequeno)
