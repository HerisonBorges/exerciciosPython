def calculoChurrasco(valor, quant):
    taxa = valor * 0.10

    return (valor + taxa) / quant


valorCarne = float(input("Qual o valor da carne? "))
quantPessoas = int(input("Qual a quantidade de pessoas? "))

valorTotal = calculoChurrasco(valorCarne,quantPessoas)

print(f"{valorTotal:.2f}")