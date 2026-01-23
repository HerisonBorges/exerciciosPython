listaTarefas = []

for _ in range(5):
    
    tarefas = input("Digite aqui a tarefa: ").lower()

    if tarefas in listaTarefas:
        print("Essa tarefa já foi anotada!")
    else:
        listaTarefas.append(tarefas)

print(listaTarefas)
listaTarefas.sort()
print(listaTarefas)