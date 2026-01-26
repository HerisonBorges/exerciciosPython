def cotaçãoDolar(dolar):

    valorEmReais = 5.10

    return dolar * valorEmReais


print("Digite o valor do produto em dolares: ")
num = float(input())
valorDoProduto = cotaçãoDolar(num)
print(f"O produto {num} custara R$: {valorDoProduto:.2f}")