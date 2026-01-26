estoque = []

for _ in range(3):
    mercado = {}

    mercado["Fruto"] = input("Digite o nome do fruto: ").lower()
    mercado["Preço"] = float(input("Digite o preço: "))

    estoque.append(mercado)

print(estoque)

busca = input("\nQual fruta você deseja consultar o preço? ").lower()
achou = False

for item in estoque:
    if item["Fruto"] == busca:
        print(f"O preço da {busca} é: R$ {item['Preço']:.2f}")
        achou = True
        break 

if not achou:
    print("A fruta não foi encontrada no estoque.")