'''Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

'''

def pedido(codigo, quantidade):

    cardapio = {
        1: 4.00,
        2: 4.50,
        3: 5.00,
        4: 2.00,
        5: 1.50
    }

    return quantidade * cardapio[codigo]


codigo = int(input())
quantidade = int(input())

total = pedido(codigo, quantidade)

print(f"Total: R$ {total:.2f}")