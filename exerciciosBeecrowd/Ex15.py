'''Timelimit: 1
Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais, segundo a fórmula:'''


import math

def distancia(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

resultado = distancia(x1, y1, x2, y2)

print(f"{resultado:.4f}")