def ordenarPorValor(dicionario):

    listaItens = dicionario.items()
    ordenarFinal = sorted(listaItens, key=lambda item: item[1], reverse=True)
    return ordenarFinal

print("Teste 1 (Frequência Decrescente):")
dados1 = {'uva': 3, 'banana': 2, 'maçã': 5, 'pera': 1}
resultado1 = ordenarPorValor(dados1)

dados2 = {'z': 5, 'y': 5, 'x': 5}
resultado2 = ordenarPorValor(dados2)

print(resultado1)
print(resultado2)

print("\nTeste 2 (Valores Iguais):")
print(resultado2)

dados3 = {}
resultado3 = ordenarPorValor(dados3)

print(f"\nTeste 3 (Dicionário Vazio): {resultado3}")