'''Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.'''


def maior(A, B, C):

    m = (A + B + abs(A - B))/2
    m = (m + C + abs(m - C)) / 2

    return f"{m} eh o maior"

A = int(input())
B = int(input())
C = int(input())

Maior = maior(A, B, C)

print(Maior)