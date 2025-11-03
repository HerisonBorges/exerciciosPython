def contarVogais(texto):
    textoMinusculo = texto.lower()  
    contador = 0                     

    for letra in textoMinusculo:    
        if letra in 'aeiou':
            contador += 1          
    return contador                 
        
texto = contarVogais("A programação em Python é legal")
print(texto)

