perguntas = ["Telefonou para a vítima?",
"Esteve no local do crime?",
"Mora perto da vítima?",
"Devia para a vítima?",
"Já trabalhou com a vítima?"]

pontuacao = 0

for pergunta in perguntas:
    print(pergunta)
    resposta = input("Digite s ou n: ").lower()
    
    if resposta == 's':
        pontuacao +=1

if pontuacao == 2:
    print("Suspeita")
elif pontuacao == 3 or pontuacao == 4:
    print("cumplice")

elif pontuacao == 5:
    print("Assassino")
else:
    print("Inocente")