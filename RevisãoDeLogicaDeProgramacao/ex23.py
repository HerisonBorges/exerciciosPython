def mediaPonderada(dados):
    somaProdutos = 0
    somaPesos = 0

    for nota, peso in dados:

        somaProdutos += nota * peso
        somaPesos += peso

    if somaPesos == 0:
        return "Soma dos pesos é zero"
    else:
        
        return somaProdutos / somaPesos
    

resultado = mediaPonderada([(10, 2), (5, 1), (8, 3)])
print(resultado)