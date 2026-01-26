def inverterOrdem(palavra):
    return palavra[::-1]


print("Digite a palavra: ")
palavra = input()

palavraInvertida = inverterOrdem(palavra)
print(palavraInvertida)
