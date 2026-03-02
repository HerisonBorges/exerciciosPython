'''Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno, sabendo que a nota A tem peso 3.5 e a nota B tem peso 7.5 (A soma dos pesos portanto é 11). Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.'''


valor1 = float(input("Digite o valor aqui: "))
valor2 = float(input("Digite o valor aqui: "))

media = (valor1 * 3.5 + valor2 * 7.5)/11

print(f"{media:.5f}")
