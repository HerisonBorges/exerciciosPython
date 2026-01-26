agenda = []

for _ in range(2):

    pessoa = {}

    pessoa["nome"] = input("Digite seu nome: ")
    pessoa["Telefone"] = int(input("Digite seu telefone: "))

    agenda.append(pessoa)

for item in agenda:
    print(f"Contato: {item['nome']} | Tel: {item['Telefone']}")


print(agenda)