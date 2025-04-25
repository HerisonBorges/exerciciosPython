dicionario = {}
backup = {}

while True:
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionario[chave]=valor

    backup[chave]=valor

    if len(dicionario)==5:
        print("Dicionario principal atingiu 5 elementos")
        for chave, valor in dicionario.items():
           print(f"{chave}: {valor}")

        dicionario.clear()
        print("Dicionario principal removido")

    continuar = input("Deseja continuar (s/n)? ").lower()

    if continuar == 'n':
        break

print("Dicionario backup")
for chave, valor in backup.items():
    print(f"{chave}: {valor}")