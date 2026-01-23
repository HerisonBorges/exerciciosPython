def emprestimoBancario(salario, parcela, tempo):

    if parcela <= salario * 0.30 and tempo > 6:
        return "APROVADO"
    else:
        return "Empréstimo Negado"

salarioPessoa = float(input("Digite o salario: "))
parcelaPessoa = float(input("Valor da parcela q vc quer pagar? "))
tempoTrabalho = int(input("Informe o tempo de trabalho: "))

emprestimo = emprestimoBancario(salarioPessoa,parcelaPessoa,tempoTrabalho)

print(emprestimo)