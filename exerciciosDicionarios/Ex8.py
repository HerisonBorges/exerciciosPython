listaDedados = []
backup = []


while len(listaDedados) < 5:
    dicionario = {}
    dicionario['nome'] = input("Digite o nome: ")
    listaDedados.append(dicionario)

print("Lista de dados")
for dicionario in listaDedados:
    for chave, valor in dicionario.items():
        print(f"{chave}, {dicionario[chave]}")  

print("Criando backup")
for dicionario in listaDedados[:]:
    listaDedados.remove(dicionario)
    backup.append(dicionario)
print(listaDedados)

print("backup dicionario")
for dicionario in backup:
    for chave in dicionario:
        print(f"{chave}, {dicionario[chave]}")