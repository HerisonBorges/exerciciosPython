def palindromo():
    palavra = input("Digite uma palavra: ")
    palavra_invertida = palavra[::-1]
    
    if palavra == palavra_invertida:
        return True
    else:
        return False
    
print(palindromo(True))