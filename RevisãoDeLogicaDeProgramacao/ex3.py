def calcularTotal(dicionario):
    dicionario["Total_Estoque"] = dicionario["quantidade"] * dicionario["valorUnitario"]


item = {}

item["nome"] = input("Digite o nome: ")
item["quantidade"] = int(input("Digite a quantidade: "))
item["valorUnitario"] = float(input("Digite o valor unitario: "))

calcularTotal(item)

print(item)