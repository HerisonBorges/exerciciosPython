'''Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).'''


def consumo (A, B):

    C = A / B

    return f"{C:.3f}"


A = int(input())
B = float(input())

cons = consumo(A, B)

print(f"{cons}")