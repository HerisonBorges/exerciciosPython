def somaMultiplos(limite):

    somaTotal = 0
    for i in range(1, limite):
        if i % 3 == 0 or i % 5  == 0:
            somaTotal+=i 

    return somaTotal


soma = somaMultiplos(10)
print(soma)