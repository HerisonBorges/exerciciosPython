def contarVogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais: # Verifica se o caractere é uma vogal
            contador += 1
    return contador

print("Digite uma frase: ")
frase = input()

totalVogais = contarVogais(frase)
print(f"A frase contém {totalVogais} vogais.")