def encontrarMaior(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print("Digite o primeiro número: ")
num1 = float(input())
print("Digite o segundo número: ")
num2 = float(input())
print("Digite o terceiro número: ")
num3 = float(input())
maior = encontrarMaior(num1, num2, num3)
print(f"O maior número entre {num1}, {num2} e {num3} é {maior}")