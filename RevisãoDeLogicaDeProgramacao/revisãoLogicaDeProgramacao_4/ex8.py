class Funcionario:

    def __init__(self, nome, cargo, salario):

        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def exibirDados(self):
        print(f"Nome: {self.nome} | Cargo atual: {self.cargo} | Salario Atual: {self.salario}")

    def promover(self, novoCargo, porcentagemAumento):

        self.cargo = novoCargo
        self.salario += (self.salario * porcentagemAumento / 100)

        print(f"Parabens! {self.nome} agora é {novoCargo}")

    
funcionario1 = Funcionario("herison", "estagiario", 2000)
funcionario1.exibirDados()
funcionario1.promover("Desenvolvedor Junior", 50)
funcionario1.exibirDados()