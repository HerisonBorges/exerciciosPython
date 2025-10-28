def reverterFrase(frase):
    palavras = frase.split() # Divide a frase em palavras
    palavras_revertidas = palavras[::-1] # Reverte a lista de palavras
    frase_revertida = ' '.join(palavras_revertidas) # Junta as palavras de volta em uma frase
    return frase_revertida # Retorna a frase revertida

print("Digite uma frase: ")
frase_input = input()
frase_revertida = reverterFrase(frase_input)
print(f"A frase revertida é: {frase_revertida}")

