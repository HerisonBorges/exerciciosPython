with open("MeuArquivo.txt", "r") as arquivo:
    for linha in arquivo:
        itemLimpo = linha.strip()
        print(f"Meta: {itemLimpo}")