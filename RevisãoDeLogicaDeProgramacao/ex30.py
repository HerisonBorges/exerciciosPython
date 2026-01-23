suaMeta = input("Qual sua meta para hoje? ")

with open("MeuArquivo.txt", "a") as arquivo:

    arquivo.write(suaMeta + "\n")

print("Pronto, aquivo salvo")