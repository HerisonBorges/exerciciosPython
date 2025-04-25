dicionario = {}

dicionario['nome'] = input("Digite o seu nome: ")
dicionario['idade'] = int(input("Digite sua idade: "))
dicionario['telefone'] = int(input("informe seu telefone: "))
dicionario['end'] = str(input("Digite seu endereço: "))



chaves = dicionario.keys()
print(chaves)

valores = dicionario.values()
print(valores)
print()

tamanho = len(dicionario)
print(tamanho)
print()

d2 = dicionario.copy()
d2['ano nascimento']=1991

print(d2)

d2.pop('ano nascimento')
print(d2)
for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")

dicionario.clear()
print(dicionario)