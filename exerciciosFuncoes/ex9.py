def potencia_interativa(a,b):
    resultado = 1
    for _ in range(b):
        resultado *= a
    return resultado

a = float(input("Digite: "))
b = int(input("Digite: "))

resultado = potencia_interativa(a,b)
print(resultado)