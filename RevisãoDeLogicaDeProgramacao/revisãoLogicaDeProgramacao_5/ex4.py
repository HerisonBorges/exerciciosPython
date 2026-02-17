class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazerSom(self):
        print("Animal faz um som")


class Cachorro(Animal):
    def fazerSom(self):
        print("Cachoro faz au au")

class Gato(Animal):
    def fazerSom(self):
        print("Gato faz miau")


meuCachorro = Cachorro("Rex")
meuCachorro.fazerSom()
meuGato = Gato("Felix")
meuGato.fazerSom()