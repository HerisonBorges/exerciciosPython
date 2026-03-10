'''Leia 4 valores inteiros A, B, C e D. A seguir, se B for maior do que C e se D for maior do que A, e a soma de C com D for maior que a soma de A e B e se C e D, ambos, forem positivos e se a variável A for par escrever a mensagem "Valores aceitos", senão escrever "Valores nao aceitos".'''


def testeSelecao(a, b, c, d):
    if (b > c and
        d > a and
        c + d > a + b and
        c > 0 and
        d > 0 and
        a % 2 == 0):
        return "Valores aceitos"
    else:
        return "Valores nao aceitos"

a = int(input())
b = int(input())
c = int(input())
d = int(input())


teste = testeSelecao(a,b,c,d)

print(teste)