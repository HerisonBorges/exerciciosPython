class Programa:
    def __init__(self, nome, ano):
        self.nome = nome
        self.ano = ano

    def exibir(self):
        print(f"Nome: {self.nome} | Ano: {self.ano}")

class Serie(Programa):
    def mostrar_tipo(self):
        print(f"Isso aqui é uma serie: {self.nome}")

minha_serie = Serie("The Office", 2005)
minha_serie.exibir()
minha_serie.mostrar_tipo()        