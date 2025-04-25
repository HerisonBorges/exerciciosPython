def contador(num,cont):
        if num > 0:
            cont += 1
        return cont


cont = 0

while True:
    num = (int(input("Digite: ")))
    if num == 0:
         break
    cont = contador(num,cont)

print("Quantidade de numeros lidos é de", cont)