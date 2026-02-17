class FuncionarioBanco:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def pagar_bonus(self):
        print(f"Pagando salario basico {self.salario} para {self.nome}")


class Diretor(FuncionarioBanco):
    def pagar_bonus(self):
        premio = 2000

        print(f"Pagando bonus de salario {self.salario + premio}, para diretor {self.nome}")


meuFuncionario = FuncionarioBanco("Cadu", 3000)
meuDiretor = Diretor("Herison", 5000)
meuFuncionario.pagar_bonus()
meuDiretor.pagar_bonus()