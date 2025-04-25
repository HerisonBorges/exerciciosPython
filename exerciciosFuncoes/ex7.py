def atualizarMaisVelho(nome, idade, nomeMaisVelho=None, idadeMaisVelho=None):
    """Atualiza e retorna o nome e idade da pessoa mais velha, se a idade atual for maior."""
    # Se idadeMaisVelho é None ou idade atual for maior, atualiza
    if idadeMaisVelho is None or idade > idadeMaisVelho:
        return nome, idade  # Retorna novo nome e idade mais velha
    return nomeMaisVelho, idadeMaisVelho  # Retorna os valores anteriores se não houver atualização

# Inicializa as variáveis para armazenar a idade e nome da pessoa mais velha
idadeMaisVelho = None  # Inicializa como None para a primeira comparação
nomeMaisVelho = None

while True:
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sair = input("Digite 's' para sair: ").lower()
    if sair == 's':
        break
    
    # Chama a função para verificar e atualizar a pessoa mais velha
    nomeMaisVelho, idadeMaisVelho = atualizarMaisVelho(nome, idade, nomeMaisVelho, idadeMaisVelho)

# Verifica se algum nome foi registrado antes de imprimir
if nomeMaisVelho is not None:
    print("A pessoa mais velha é:", nomeMaisVelho, "com idade de:", idadeMaisVelho)
else:
    print("Nenhuma pessoa encontrada")




    
    