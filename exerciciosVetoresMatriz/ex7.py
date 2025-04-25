numeros = [10, 2, 8, 6, 7, 3]

numeros_ordenados =  sorted(numeros)
print(numeros_ordenados)

palavras = ["banana", "kiwi", "laranja", "uva", "abacaxi"]
palavrasOrdenada = sorted(palavras)
print(palavrasOrdenada)


tuplas = [(1, 3), (2, 1), (5, 7)]

tuplasOrdenadas = sorted(tuplas, key=lambda x: x[1])
print(tuplasOrdenadas)

idades = {"Ana": 23, "Pedro": 30, "João": 22, "Mariana": 27}
dicionarioOrdenado = sorted(idades.items(), key=lambda x: x [1])
print(dicionarioOrdenado)

palavras = ["gato", "elefante", "cachorro", "abelha", "zebra"]
palavrasUltimaLetra = sorted(palavras, key=lambda x: x[-1])
print(palavrasUltimaLetra)

listas = [[3, 2, 1], [5, 0, 2], [1, 4, 6], [2, 8, 7]]

listaOrdenadaPrimeiroNumero = sorted(listas, key=lambda x: x[0])
print(listaOrdenadaPrimeiroNumero)

notas = {"Ana": 85, "Pedro": 92, "João": 78, "Mariana": 88}
ordenado = sorted(notas.items(), key=lambda x: x[1])
print(ordenado)