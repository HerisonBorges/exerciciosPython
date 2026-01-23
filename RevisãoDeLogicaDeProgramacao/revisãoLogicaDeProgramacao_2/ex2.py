def preçoIngresso(idade):

    if idade < 18:
        return "Entrada Proibida"
    elif 18 <= idade <= 21:
        return "Entrada liberada! Ingresso: R$ 20,00"
    else:
        return "Entrada liberada! Ingresso: R$ 30,00"
    

idade = int(input("Digite sua idade: "))
idadeUsuario = preçoIngresso(idade)
print(idadeUsuario)