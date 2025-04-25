def contador(num,cont):
    if num > 0:
        cont += 1
    return cont
def somaNum(num,soma):
    soma += num
    return soma
def maiorMenorNumero(num,maiorNumero,menorNumero):
    if num > maiorNumero:
        maiorNumero = num

    if num < menorNumero:
        menorNumero = num
    return maiorNumero, menorNumero


soma = 0
cont = 0
maiorNumero = -1
menorNumero = 1001
while True:
    num = int(input("Digite "))
    if num == 0:
        break
    cont = contador(num,cont)
    soma = somaNum(num,soma)
    maiorNumero, menorNumero = maiorMenorNumero(num,maiorNumero,menorNumero)
if cont > 0:
    media = soma / cont
else:
    media = 0

print(maiorNumero)
print(menorNumero)
print(cont)  
print(soma)  
print(media)