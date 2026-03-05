'''Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.'''

def conversor(n):

    horas = n // 3600
    minutos = (n % 3600) // 60
    segundos = (n % 3600) % 60

    return f"{horas}:{minutos}:{segundos}"


numero = int(input())

converterNum = conversor(numero)

print(converterNum)