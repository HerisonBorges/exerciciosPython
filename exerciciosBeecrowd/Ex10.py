'''Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.'''


total = 0

for _ in range(2):
    codigoPeca = int(input("Digite o codigo: "))
    numeroPecas = int(input("Digite o numero de peças: "))
    valorUnitario = float(input("Informe o valor unitario: "))

    total = total + (numeroPecas * valorUnitario)

print(total)

   
