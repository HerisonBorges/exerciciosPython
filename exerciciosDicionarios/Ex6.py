listaDeDados = []

while True:    
    dicionario = {}
    dicionario['nome'] = input("Digite o seu nome: ")
    dicionario['idade'] = int(input("Digite sua idade: "))
    dicionario['telefone'] = int(input("informe seu telefone: "))
    dicionario['end'] = str(input("Digite seu endereço: "))
    listaDeDados.append(dicionario)
    sair = input("Digite sair para finalizar: ").strip().lower()
    if sair == 'sair':
        break
for dicionario in listaDeDados:
    for chave in dicionario:
        print(f"{chave}: {dicionario[chave]}")