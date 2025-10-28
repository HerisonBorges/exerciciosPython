def gerarFibonacci(num):
    sequencia = [0, 1] # Sequência inicial
    while len(sequencia) < num:# Gera até o número desejado
        proximo = sequencia[-1] + sequencia[-2]# Próximo número é a soma dos dois últimos
        sequencia.append(proximo)
    return sequencia[:num]

print("Digite a quantidade: ")
quantidade = int(input())
fibonacci = gerarFibonacci(quantidade)
print(f"A sequência de Fibonacci com {quantidade} termos é: {fibonacci}")