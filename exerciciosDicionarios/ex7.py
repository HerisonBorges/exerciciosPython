listaDeDados = []
dadosMenores18 = []
while True:
    dicionario = {}
    dicionario['nome'] = input("Digite o nome: ")
    dicionario['idade'] = int(input("Digite a idade: "))
    dicionario['cpf'] = float(input("Digite o cpf: "))
    listaDeDados.append(dicionario)
    if input("Digite 'sair' ou qualquer tecla para continuar: "):
        break
    

for dicionario in listaDeDados[:]:
    if dicionario["idade"] < 18:
        dadosMenores18.append(dicionario)
        listaDeDados.remove(dicionario)

print("Lista de dados")
for dicionario in listaDeDados:
    for chave in dicionario:
        print(f"{chave}: {dicionario[chave]}")
        
print("Lista de dados menores de 18: " )
for dicionario in dadosMenores18:
    for chave in dicionario:
        print(f"{chave}: {dicionario[chave]}")