notas = []

for _ in range(4):
    notasAlunos = float(input("Digite a nota do aluno: "))
    notas.append(notasAlunos)

aprovados = []

for item in notas:
    if item >= 7:
        aprovados.append(item)

print(notas)
print(len(aprovados))