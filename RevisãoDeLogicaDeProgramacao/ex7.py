class Livro:
    
    def __init__(self, titulo, autor):

        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):

        if self.disponivel == True:
            self.disponivel = False

            print(f"O livro {self.titulo} emprestado")

        else:
            print(f"O livro {self.titulo} já está alugado.")



meuLivro = Livro("Fanged Noumena", "Nick Land")
meuLivro.emprestar()
meuLivro.emprestar()