sudoku_valido = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_invalido = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 1, 9]  
]

valido = True
for linha in sudoku_valido:
    if sorted(linha) != list(range(1, 10)):
        valido = False
        break

for col in range(9):
    coluna = [sudoku_valido[linha][col] for linha in range(9)]
    if sorted(coluna) != list(range(1, 10)):
        valido = False
        break

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        bloco = [sudoku_valido[x][y] for x in range(i, i+3) for y in range(j, j+3)]
        if sorted(bloco) != list(range(1, 10)):
            valido = False
            break


print("sudoku válido:", valido)


valido = True

for linha in sudoku_invalido:
    if sorted(linha) != list(range(1, 10)):
        valido = False
        break

for col in range(9):
    coluna = [sudoku_invalido[linha][col] for linha in range(9)]
    if sorted(coluna) != list(range(1, 10)):
        valido = False
        break