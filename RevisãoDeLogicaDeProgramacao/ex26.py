def mediaNotas(nota1, nota2, nota3):

    media = nota1 + nota2 +nota3 / 3

    print(f"{media:.2f}")

    if media >= 7:
        return "Aprovado! Parabéns!"
    elif media >= 5 and media <= 6.9:
        return "Em Recuperação. Estude um pouco mais."
    else:
       return "Reprovado."

print("Primeira nota: ")
num1 = float(input())
print("Segunda nota: ")
num2 = float(input())
print("Terceira nota: ")
num3 = float(input())

resultadoFinal = mediaNotas(num1,num2,num3)

print(resultadoFinal)