while True:

    desejos = input("desejo de consumo: (digite s para sair) ")

    if desejos == 's':
        break

    with open("desejos.txt", "a") as arquivo:
        arquivo.write(desejos + "\n")

    
    print("Pronto, aquivo salvo")


print("---MEUS DESEJOS CADASTRADOS---")


try:
    with open("desejos.txt", "r") as arquivo:
        for linha in arquivo:
            itemLimpo = linha.strip()

            print(f"-> {itemLimpo}")

except FileNotFoundError:
    print("Aviso: O arquivo ainda não existe no seu computador.")