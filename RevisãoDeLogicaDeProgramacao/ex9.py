gastos = []

for _ in range(3):
    despesas = {}

    despesas["Nome"] = input("Digite o nome: ")
    despesas["Valor"] = float(input("Digite o valor: "))

    gastos.append(despesas)

print (gastos)

total = 0

for item in gastos:
    total += item["Valor"]

print(total)