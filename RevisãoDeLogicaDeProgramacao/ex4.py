class Carro:
    def __init__(self, modelo, marca):
        self.modelo = modelo
        self.marca = marca
        
    def exibirDados(self):
        print(f"Carro: {self.modelo} | Fabricante: {self.marca}")


meuCarro = Carro("Gol", "Wolkswagen")
meuCarro.exibirDados()