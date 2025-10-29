def calcularMedia(notas):
    return sum(notas) / len(notas)


listaDeNotas = []

while True:

    entrada = input("Digite uma nota (ou 'sair' para encerrar): ")
    
    if entrada.lower() == 'sair':
        break
    try:
        nota = float(entrada)
        listaDeNotas.append(nota)
    except ValueError:
        print("Favor digitar um numero valido, ou digite 'sair': ")


print(listaDeNotas)

if len(listaDeNotas) > 0:

    media = calcularMedia(listaDeNotas)
    print(media)

else:
    print("Não foi encontrado nenhum numero na lista ")




