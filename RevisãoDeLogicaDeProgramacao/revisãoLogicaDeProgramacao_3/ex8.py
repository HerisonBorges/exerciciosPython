aluno = {}

aluno["Nome"] = input("Digite o nome: ")
aluno["Nota1"] = float(input("Digite a primeira nota: "))
aluno["Nota2"] = float(input("Digite a segunda nota: "))

print(aluno)

aluno["Media"] = (aluno["Nota1"] + aluno["Nota2"]) / 2

print (aluno)

if aluno["Media"] >= 7:
    aluno["Situação"] = "Aprovado"

else: 
    aluno["Situação"] = "Reprovado"

print(aluno)