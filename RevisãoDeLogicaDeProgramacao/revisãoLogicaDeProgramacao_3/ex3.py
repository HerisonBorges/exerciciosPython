agenda = []

for _ in range(2):
    
    pessoa = {}

    pessoa["nome"] = input("Digite seu nome: ")
    pessoa["Telefone"] = int(input("Digite seu telefone: "))

    agenda.append(pessoa)



print(agenda)