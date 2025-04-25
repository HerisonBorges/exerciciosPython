dicionario = {
    "Nome": "Herison",
    "Idade": 33,
    "Curso": "Sistemas de Informação",
    "Ano de nascimento": 1991,
 }


print(dicionario["Ano de nascimento"])
print(len(dicionario))

pessoa = {
    "Nome": "Teste",
    "Idade": 0,
    "Peso": 0.0
}

print("Dados da pessoa")
print("Nome:", pessoa["Nome"])
print("Peso:", pessoa["Peso"])
print("Idade:", pessoa["Idade"])
print()
 
print("Usuario informando os dados")
pessoa["Nome"] = input("Digite seu nome: ")
pessoa["Peso"] = float(input("Digite seu peso: "))
pessoa["Idade"] = int(input("Digite sua idade: "))

print("Nome:", pessoa["Nome"])
print("Peso:", pessoa["Peso"])
print("Idade:", pessoa["Idade"])
print()

listaPessoas = []
for _ in range(3):
    pessoa = {}
    pessoa["Nome"] = input("Digite seu nome: ")
    pessoa["Peso"] = float(input("Digite seu peso: "))
    pessoa["Idade"] = int(input("Digite sua idade: "))
    listaPessoas.append(pessoa)

print("Dados das pessoas:")

for pessoa in listaPessoas:
    print("Nome:", pessoa["Nome"])
    print("Peso:", pessoa["Peso"])
    print("Idade:", pessoa["Idade"])
    print()

listaProdutos = []
contadorPordutos = 0

while contadorPordutos < 5:
    produtos = {}
    produtos["nIndentificação"] = int(input("Digite o numero de indentificação: "))
    produtos["nomeProduto"] = input("informe o nome do produto: ")
    produtos["preco"] = float(input("Digite o preço: "))
    listaProdutos.append(produtos)
    contadorPordutos+=1
    print("Quantidade de produtos ate o momento é de ", contadorPordutos)
  

for produtos in listaProdutos:
    print("Id produto", produtos["nIndentificação"])
    print("Nome do produto", produtos["nomeProduto"])
    print("Preço do produto", produtos["preco"])
    print()