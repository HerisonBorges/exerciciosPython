'''Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.'''


numeroFuncionario = int(input("Digite o numero: "))
numeroHorasTrabalhadas = int(input("Digite o numero: "))
valorPorHora = float(input("Digite o valor: "))

Salario = numeroHorasTrabalhadas * valorPorHora

print(numeroFuncionario)
print(f"{Salario:.2f}")