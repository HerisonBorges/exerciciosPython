def saoAnagramas(palavra1, palavra2):
    return sorted(palavra1) == sorted(palavra2) # Verifica se as palavras são anagramas ou não ao ordenar seus caracteres

print("Digite a primeira palavra: ")
palavra1 = input()
print("Digite a segunda palavra: ")
palavra2 = input()

if saoAnagramas(palavra1, palavra2):
    print(f"As palavras '{palavra1}' e '{palavra2}' são anagramas.")
else:
    print(f"As palavras '{palavra1}' e '{palavra2}' não são anagramas.")

    