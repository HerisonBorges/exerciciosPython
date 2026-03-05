'''
Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias

Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.'''

def conversorIdade(idade):

    ano = idade // 365
    idade = idade % 365
    mes = idade // 30
    dias = idade % 30

    return f"{ano}:{mes}:{dias}"


numero = int(input())

converterNum = conversorIdade(numero)

print(converterNum)