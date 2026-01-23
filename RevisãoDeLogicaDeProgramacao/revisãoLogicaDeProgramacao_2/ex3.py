def calculadoraIMC(peso, altura):
    imc =  peso/(altura*altura)

    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        return "Peso normal"
    elif 24.9 <= imc <= 29.9:
        return "Sobrepeso"
    else:
       return "Obesidade"

pesoPessoa = float(input("Digite o peso: "))
alturaPessoa = float(input("Digite a altura: "))

valorImc = calculadoraIMC(pesoPessoa,alturaPessoa)
print(valorImc)