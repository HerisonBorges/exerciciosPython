def calcularFatorial(n):
    if n < 0:
        return "Erro"
    elif n == 0:
        return 1
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i
    return fatorial

num = int(input("Digite um numero: "))
fatorial = calcularFatorial(num)
print(fatorial)