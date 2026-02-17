class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def detalhes(self):
        print(f"Nome: {self.nome} | Salario: {self.salario} ")
         
meuFuncionario = Funcionario("Herison", 2500)
meuFuncionario.detalhes()

class Gerente(Funcionario):
        def aumentar(self):
            self.salario += 500

meu_gerente = Gerente("Herison", 2500)
meu_gerente.aumentar()
meu_gerente.detalhes()


class Estagiario(Funcionario):
        def estudar(self):
            print(f"O estagiario {self.nome} está aprendendo Python")

        def aumentar(self):
            self.salario +=100

estagiario1 = Estagiario("João", 1000)
estagiario1.detalhes()
estagiario1.aumentar()
estagiario1.detalhes()
