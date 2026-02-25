class Aluno:
    def __init__(self, aluno):
        self.aluno = aluno
        self.notas = []

    def adcionarNota(self, n):
        self.notas.append(n)

    def media(self):
        soma = 0
        for i in self.notas:
            soma += i

        if len(self.notas) > 0:
            m = soma / len(self.notas)
            return m
        
    def mostrar(self):
    
        m = self.media()
        print(f"Aluno: {self.aluno}")
        print(f"Média: {m}")



a1 = Aluno("Ana")
a1.adcionarNota(7)
a1.adcionarNota(9)

a2 = Aluno("Pedro")
a2.adcionarNota(5)

a1.mostrar()
a2.mostrar()