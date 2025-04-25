def somaImpar(num,soma):
    if num%3 ==0:
        if num % 2 != 0:
            soma+=num
    return soma

soma = 0 
for num in range(501):
    
    
    soma = somaImpar(num,soma)
print(soma)
        