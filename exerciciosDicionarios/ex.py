#____________________________________DICIONARIOS
'''dicionario = {
    "Nome": "Herison",
    "Idade": 33,
    "Curso": "Sistemas de Informação",
    "Ano de nascimento": 1991,
 }


print(dicionario["Ano de nascimento"])
print(len(dicionario))'''

'''pessoa = {
    "Nome": "Teste",
    "Idade": 0,
    "Peso": 0.0
}

print("Dados da pessoa")
print("Nome:", pessoa["Nome"])
print("Peso:", pessoa["Peso"])
print("Idade:", pessoa["Idade"])
print()
 
print("Usuario informando os dados")
pessoa["Nome"] = input("Digite seu nome: ")
pessoa["Peso"] = float(input("Digite seu peso: "))
pessoa["Idade"] = int(input("Digite sua idade: "))

print("Nome:", pessoa["Nome"])
print("Peso:", pessoa["Peso"])
print("Idade:", pessoa["Idade"])
print()'''


'''listaPessoas = []
for _ in range(3):
    pessoa = {}
    pessoa["Nome"] = input("Digite seu nome: ")
    pessoa["Peso"] = float(input("Digite seu peso: "))
    pessoa["Idade"] = int(input("Digite sua idade: "))
    listaPessoas.append(pessoa)

print("Dados das pessoas:")

for pessoa in listaPessoas:
    print("Nome:", pessoa["Nome"])
    print("Peso:", pessoa["Peso"])
    print("Idade:", pessoa["Idade"])
    print()'''

'''listaProdutos = []
contadorPordutos = 0

while contadorPordutos < 5:
    produtos = {}
    produtos["nIndentificação"] = int(input("Digite o numero de indentificação: "))
    produtos["nomeProduto"] = input("informe o nome do produto: ")
    produtos["preco"] = float(input("Digite o preço: "))
    listaProdutos.append(produtos)
    contadorPordutos+=1
    print("Quantidade de produtos ate o momento é de ", contadorPordutos)
  

for produtos in listaProdutos:
    print("Id produto", produtos["nIndentificação"])
    print("Nome do produto", produtos["nomeProduto"])
    print("Preço do produto", produtos["preco"])
    print()'''

#__________________________________________________exercicios e exemplos

'''tel = {'carlos': 4098, 'sergio': 4139}
#inserindo nova chave e valor
tel['guido'] = 4127
tel['irving'] = 4127
tel['pedro'] = 8712
print(tel)'''
#_____________________________________________________________________________
'''dicionario = {'nome': "Herison", 'idade': 33, 'tel': 222, 'end': "Rua dos tito"}
print(dicionario['nome'])'''

#_____________________________________________________________________ex-1
'''dicionario = {}

dicionario['nome'] = input("Digite o seu nome: ")
dicionario['idade'] = int(input("Digite sua idade: "))
dicionario['telefone'] = int(input("informe seu telefone: "))
dicionario['end'] = str(input("Digite seu endereço: "))

for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")'''

#________________________________________________________________________ex-2
'''dicionario = {}

dicionario['nome'] = input("Digite o seu nome: ")
dicionario['idade'] = int(input("Digite sua idade: "))
dicionario['telefone'] = int(input("informe seu telefone: "))
dicionario['end'] = str(input("Digite seu endereço: "))



chaves = dicionario.keys()
print(chaves)

valores = dicionario.values()
print(valores)
print()

tamanho = len(dicionario)
print(tamanho)
print()

d2 = dicionario.copy()
d2['ano nascimento']=1991

print(d2)

d2.pop('ano nascimento')
print(d2)
for chave in dicionario:
    print(f"{chave}: {dicionario[chave]}")

dicionario.clear()
print(dicionario)'''

#__________________________________________________________________ex - 3

'''listaDeDados = []

while True:    
    dicionario = {}
    dicionario['nome'] = input("Digite o seu nome: ")
    dicionario['idade'] = int(input("Digite sua idade: "))
    dicionario['telefone'] = int(input("informe seu telefone: "))
    dicionario['end'] = str(input("Digite seu endereço: "))
    listaDeDados.append(dicionario)
    sair = input("Digite sair para finalizar: ").strip().lower()
    if sair == 'sair':
        break
for dicionario in listaDeDados:
    for chave in dicionario:
        print(f"{chave}: {dicionario[chave]}")'''

#__________________________________________________________________ex-4

'''listaDeDados = []
dadosMenores18 = []
while True:
    dicionario = {}
    dicionario['nome'] = input("Digite o nome: ")
    dicionario['idade'] = int(input("Digite a idade: "))
    dicionario['cpf'] = float(input("Digite o cpf: "))
    listaDeDados.append(dicionario)
    if input("Digite 'sair' ou qualquer tecla para continuar: "):
        break
    

for dicionario in listaDeDados[:]:
    if dicionario["idade"] < 18:
        dadosMenores18.append(dicionario)
        listaDeDados.remove(dicionario)

print("Lista de dados")
for dicionario in listaDeDados:
    for chave in dicionario:
        print(f"{chave}: {dicionario[chave]}")
        
print("Lista de dados menores de 18: " )
for dicionario in dadosMenores18:
    for chave in dicionario:
        print(f"{chave}: {dicionario[chave]}")'''

#________________________________________________________________________ex-5
#versao 1
'''listaDedados = []
backup = []


while len(listaDedados) < 5:
    dicionario = {}
    dicionario['nome'] = input("Digite o nome: ")
    listaDedados.append(dicionario)

print("Lista de dados")
for dicionario in listaDedados:
    for chave, valor in dicionario.items():
        print(f"{chave}, {dicionario[chave]}")  

print("Criando backup")
for dicionario in listaDedados[:]:
    listaDedados.remove(dicionario)
    backup.append(dicionario)
print(listaDedados)

print("backup dicionario")
for dicionario in backup:
    for chave in dicionario:
        print(f"{chave}, {dicionario[chave]}")  '''
#______________________________________________________________________ex-6

'''dicionario = {}
backup = {}

while True:
    chave = input("Digite a chave: ")
    valor = input("Digite o valor: ")
    dicionario[chave]=valor

    backup[chave]=valor

    if len(dicionario)==5:
        print("Dicionario principal atingiu 5 elementos")
        for chave, valor in dicionario.items():
           print(f"{chave}: {valor}")

        dicionario.clear()
        print("Dicionario principal removido")

    continuar = input("Deseja continuar (s/n)? ").lower()

    if continuar == 'n':
        break

print("Dicionario backup")
for chave, valor in backup.items():
    print(f"{chave}: {valor}")'''


#_______________________________________________________ex6

'''listaDeDados = []
while True:
    dicionario = {}

    chave = input("Digite uma chave: ")
    valor = input("Digite um valor: ")
    finalizar = input("Digite 'sair' para finalizar: ").lower()
    dicionario[chave]=valor
    listaDeDados.append(dicionario)
    if finalizar == 'sair':
        print("Porgrama finalizado")
        break
print("lista de dicionarios")
for dicionario in listaDeDados:
        print(dicionario)'''

#__________________________________________________ex6

'''listaDeConjuntos = []
conjunto = set()
while True:
    valor = int(input("Digite um valor: "))
    conjunto.add(valor)
    listaDeConjuntos.append(conjunto)
    finalizar = input("Digite 'sair' para finalizar: ").lower()
    
    if finalizar == 'sair':
        break

print(conjunto)'''

#__________________________________________________ex7

'''MATRIZ DE DICIONARIOS'''
'''matriz = []
somaPares = 0
somaImpares = 0
linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))
for i in range(linhas):
    linhaAtual = []
    for j  in range(colunas):
        elemento = int(input(f"Digite o numero {i} {j}: "))
        linhaAtual.append(elemento)
        if elemento % 2 == 0:
            somaPares += elemento
        else:
            somaImpares += elemento
    matriz.append(linhaAtual)
for linha in matriz:
    print(linha)

print(somaPares)
print(somaImpares)'''


#___________________________________________________ex8

'''matriz = []
linhas = int(input("Digite o número de linhas da primeira matriz: "))
colunas = int(input("Digite o número de colunas da primeira matriz: "))
for i in range(linhas):
    linha_atual = []
    for j in range(colunas):
        elemento = int(input(f"Digite o número para a posição ({i},{j}): "))
        linha_atual.append(elemento)
    matriz.append(linha_atual)

print("\nPrimeira matriz:")
for linha in matriz:
    print(linha)

linhas2 = int(input("Digite o número de linhas da segunda matriz: "))
colunas2 = int(input("Digite o número de colunas da segunda matriz: "))
matriz2 = []

for i in range(linhas2):
    linha_atual2 = []
    for j in range(colunas2):
        elemento = int(input(f"Digite o número para a posição ({i},{j}): "))
        linha_atual2.append(elemento)
    matriz2.append(linha_atual2)

print("\nSegunda matriz:")
for linha in matriz2:
    print(linha)

# Verificando se a multiplicação é possível
if colunas != linhas2:
    print("Erro: O número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
else:
    matriz_resultado = [[0] * colunas2 for _ in range(linhas)]

    
    for i in range(linhas):
        for j in range(colunas2):
            for k in range(colunas):  # Ou k em range(linhas2) (que é igual a colunas)
                matriz_resultado[i][j] += matriz[i][k] * matriz2[k][j]

    # Exibindo a matriz resultante
    print("\nMatriz resultante da multiplicação:")
    for linha in matriz_resultado:
        print(linha)'''

#____________________________________________________________________ex9


'''matriz = [[],[],[]]
lista = []
for i in range(3):
    soma = 0
    for j in range(4):
        numero = int(input(f"Insira um numero inteiro na linha {i} coluna {j}\n"))
        matriz[i].append(numero)
        soma += numero
    lista.append(soma)

matriz_2 = [[],[],[]]

for i in range(3):
    for elemento in matriz[i]:
        mult = elemento * lista[i]
        matriz_2[i].append(mult)
        
for i in matriz_2:
    print(i)'''

#_________________________________________________________________________ex10

'''lista = []

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

print(lista)'''

'''imagem = [
    [0, 255, 256, 68],
    [0, 255, 256, 68],
    [0, 255, 256, 68]
]'''




'''matriz = []

houveplantação = []
semPlantacao = []
indeterminado = []


linhas = int(input("Digite o numero de linhas: "))
colunas = int(input("Digite o numero de colunas: "))

for x in range(linhas):
    linha_atual = []
    for y in range(colunas):
        elemento = int(input(f"Digite o valor do elemento {x} {y}: "))
        linha_atual.append(elemento)
    matriz.append(linha_atual)


for x in range(len(matriz)):
    for y in range(len(matriz[x])):
        valorPixel = matriz[x][y]

        if valorPixel > 120:
            houveplantação.append((x,y))
        elif valorPixel < 30:
            semPlantacao.append((x,y))
        else:
            indeterminado.append((x,y))

print("houve plantação:", houveplantação)
print("nao houve plantação:", semPlantacao)
print("não é possível determinar:", indeterminado)'''


'''sudoku_valido = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_invalido = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 1, 9]  
]

valido = True
for linha in sudoku_valido:
    if sorted(linha) != list(range(1, 10)):
        valido = False
        break

for col in range(9):
    coluna = [sudoku_valido[linha][col] for linha in range(9)]
    if sorted(coluna) != list(range(1, 10)):
        valido = False
        break

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        bloco = [sudoku_valido[x][y] for x in range(i, i+3) for y in range(j, j+3)]
        if sorted(bloco) != list(range(1, 10)):
            valido = False
            break


print("sudoku válido:", valido)


valido = True

for linha in sudoku_invalido:
    if sorted(linha) != list(range(1, 10)):
        valido = False
        break

for col in range(9):
    coluna = [sudoku_invalido[linha][col] for linha in range(9)]
    if sorted(coluna) != list(range(1, 10)):
        valido = False
        break

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        bloco = [sudoku_invalido[x][y] for x in range(i, i+3) for y in range(j, j+3)]
        if sorted(bloco) != list(range(1, 10)):
            valido = False
            break
print("Sudoku inválido:", valido)'''


'''numeros = [10, 2, 8, 6, 7, 3]

numeros_ordenados =  sorted(numeros)
print(numeros_ordenados)'''

'''palavras = ["banana", "kiwi", "laranja", "uva", "abacaxi"]
palavrasOrdenada = sorted(palavras)
print(palavrasOrdenada)
'''

'''tuplas = [(1, 3), (2, 1), (5, 7)]

tuplasOrdenadas = sorted(tuplas, key=lambda x: x[1])
print(tuplasOrdenadas)'''

'''idades = {"Ana": 23, "Pedro": 30, "João": 22, "Mariana": 27}
dicionarioOrdenado = sorted(idades.items(), key=lambda x: x [1])
print(dicionarioOrdenado)'''

'''palavras = ["gato", "elefante", "cachorro", "abelha", "zebra"]
palavrasUltimaLetra = sorted(palavras, key=lambda x: x[-1])
print(palavrasUltimaLetra)'''

'''listas = [[3, 2, 1], [5, 0, 2], [1, 4, 6], [2, 8, 7]]

listaOrdenadaPrimeiroNumero = sorted(listas, key=lambda x: x[0])
print(listaOrdenadaPrimeiroNumero)'''

'''notas = {"Ana": 85, "Pedro": 92, "João": 78, "Mariana": 88}
ordenado = sorted(notas.items(), key=lambda x: x[1])
print(ordenado)'''


#___________________________________________________________________________

'''matriz = []
cont = 1
somapar = 0
somaImpar = 0
for i in range(3):
    linha= []
    for j in range(3):
        linha.append(cont)
        if cont % 2 == 0:
            somapar += cont
        else:
            somaImpar += cont
        cont += 1
    matriz.append(linha)
for linha in matriz:
   print(linha)

print()
print(somapar)
print(somaImpar)'''
#________________________________________________________________
'''matriz = []
cont = 1

for i in range(4):
    linha=[]
    for j in range(4):
        linha.append(cont)
        cont += 1
    matriz.append(linha)

for linha in matriz:
    print(linha)
print()
matriz[1], matriz [2] = matriz[2], matriz[1]
for i in range(4):

    matriz[i][0], matriz[i][3] = matriz[i][3], matriz[i][0]
print()

for linha in matriz:
    print(linha)'''
#________________________________________________________

matriz = []
cont = 1

for i in range(4):
    linha=[]
    for j in range(4):
        linha.append(cont)
        cont += 1
    matriz.append(linha)

for linha in matriz:
    print(linha)

for i, linha in enumerate(matriz, start = 1):
    soma = sum(linha)
    print(f"Media de cada linha {i}: {soma}")