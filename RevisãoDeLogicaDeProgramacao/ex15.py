def estaNoIntervalo(numero, limiteMin, limiteMax):
    if numero >= limiteMin and numero <= limiteMax:
        return True
    else:
        return False
    
limiteMinimo = int(input("Digite o limite minimo: "))
limiteMaximo = int(input("Digite o limite maximo: "))

num = int(input("Digite o numero para verificar: "))

intervalo = estaNoIntervalo(num, limiteMinimo, limiteMaximo)
print(intervalo)