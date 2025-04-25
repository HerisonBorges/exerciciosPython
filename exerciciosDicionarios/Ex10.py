listaDeDados = []
while True:
    dicionario = {}

    chave = input("Digite uma chave: ")
    valor = input("Digite um valor: ")
    finalizar = input("Digite 'sair' para finalizar: ").lower()
    dicionario[chave]=valor
    listaDeDados.append(dicionario)
    if finalizar == 'sair':
        print("Porgrama finalizado")
        break
print("lista de dicionarios")
for dicionario in listaDeDados:
        print(dicionario)