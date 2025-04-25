def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i
    return resultado

numero = int(input("Digite: "))
res = fatorial(numero)
print(res)