dicionario = {}

dicionario['nome'] = input("Digite o seu nome: ")
dicionario['idade'] = int(input("Digite sua idade: "))
dicionario['telefone'] = int(input("informe seu telefone: "))
dicionario['end'] = str(input("Digite seu endereço: "))

for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")