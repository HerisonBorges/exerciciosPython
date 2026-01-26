gastos = []

for _ in range(3):
    despesas = {}

    despesas["Nome"] = input("Digite o nome: ")
    despesas["Valor"] = float(input("Digite o valor: "))

    gastos.append(despesas)

print(gastos)

total = 0
maiorValor = 0
nomeDoMaisCaro = 0

for item in gastos:
    total += item["Valor"]

    if item["Valor"] > maiorValor:
        maiorValor = item["Valor"]
        nomeDoMaisCaro = item["Nome"]

print(f"{total:.2f}")
print(f"{nomeDoMaisCaro}, {maiorValor}")

