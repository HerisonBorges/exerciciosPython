lista = []

while True:
    print("Menu")
    print("Digite 'a' para adicionar um novo cadastro: ")
    print("Digite 'b' para remover um cadastro: ")
    print("Digite 'c' para apresentar em ordem alfabetica: ")
    print("Dgite 'd' para sair do programa")
    opcao = input("Escolha um opção: ").lower()

    if opcao == 'a':
        nome = input("Digite o nome: ").lower()
        idade = int(input("Digite a idade: "))
        matricula = int(input("Digite a matricula: "))

        cadastro = {"nome": nome, "idade": idade, "matricula": matricula}
        lista.append(cadastro)
        print("Cadastro realizado com sucesso!")

    elif opcao == 'b':
        nomeRemovido = input("Digite o nome do cadastro que deseja remover: ")
        for cadastro in lista:
            if cadastro["nome"].lower() == nomeRemovido.lower():
                lista.remove(cadastro)
        print("Cadastro removido com sucesso: ")

    elif opcao == 'c':
        nomesOrdenado = sorted(lista, key=lambda x: x["nome"].lower())
        for cadastro in nomesOrdenado:
            print(f"Nome:{cadastro['nome']}, Idade:{cadastro['idade']}, Matricula: {cadastro['matricula']}")
    elif opcao == 'd':
        print("Finalizando programa")
        break

print(lista)