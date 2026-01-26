def verificarParOuImpar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"
    
print("Digite um número inteiro: ")
num = int(input())
resultado = verificarParOuImpar(num)
print(f"O número {num} é {resultado}")