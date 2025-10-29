def contarCaractere(texto, caractereAlvo):
    numeroCaracteres = texto.count(caractereAlvo)
    return numeroCaracteres

while True:
    entrada = input("Digite o texto (ou '1' para sair): ")
    
    if entrada == '1':
        break

    caractere = input("Qual caractere você quer contar? ")

    contador = contarCaractere(entrada, caractere)
    print(f"O caractere '{caractere}' aparece {contador} vezes em \"{entrada}\".\n")
