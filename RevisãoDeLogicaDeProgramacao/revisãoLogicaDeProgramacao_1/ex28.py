produto = {}

produto["nome"] = input("Informe o nome do produto: ")
produto["preço"] = float(input("Informe o nome preço: "))
produto["estoque"] = float(input("Digite a quantidade do estoque: "))


print(f"O produto {produto['nome']} custa R$ {produto['preço']} e temos {produto['estoque']} unidades.")