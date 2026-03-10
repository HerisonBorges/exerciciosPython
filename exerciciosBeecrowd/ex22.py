'''Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.'''

import math

def formulaBhaskara(a, b, c):

    delta = b*b - 4*a*c

    if delta < 0 or a == 0:
        print("Impossivel calcular")
    else:
        r1 = (-b + math.sqrt(delta)) / (2 * a)
        r2 = (-b - math.sqrt(delta)) / (2 * a)

        print(f"{r1:.5f}")
        print(f"{r2:.5f}")


a = float(input())
b = float(input())
c = float(input())

formulaBhaskara(a, b, c)