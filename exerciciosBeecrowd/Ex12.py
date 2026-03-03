'''Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.'''


def area_triangulo(a, c):
    return (a * c) / 2

def area_circulo(c):
    return 3.14159 * (c ** 2)

def area_trapezio(a, b, c):
    return ((a + b) * c) / 2

def area_quadrado(b):
    return b ** 2

def area_retangulo(a, b):
    return a * b

A = float(input())
B = float(input())
C = float(input())

print(f"{area_triangulo(A, C):.3f}")
print(f"{area_circulo(C):.3f}")
print(f"{area_trapezio(A, B, C):.3f}")
print(f"{area_quadrado(B):.3f}")
print(f"{area_retangulo(A, B):.3f}")