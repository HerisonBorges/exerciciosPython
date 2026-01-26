aluno = {}

aluno["nome"] = input("Digite o nome do aluno: ")
aluno["media"] = float(input("Digite a media desse aluno: "))


if aluno["media"] >= 7:
    aluno["Situação"] = "Aprovado"

else:
    aluno["Situação"] = "Reprovado"


print(f"O aluno {aluno['nome']} está {aluno['Situação']}!")

print(aluno)

del aluno["media"]

print (aluno)