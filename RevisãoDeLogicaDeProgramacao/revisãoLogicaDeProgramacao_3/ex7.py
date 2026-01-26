
placar = {"time_a": 0, "time_b": 0}

for _ in range(3):
    quemMarcou = input("Digite quem marcou o gol: ")
    if quemMarcou == 'a':
        placar["time_a"] +=1
    else:
        placar["time_b"] +=1

print(placar)