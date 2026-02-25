class Playlist:
    def __init__(self):
        self.musicas = []

    def adicionarMusica(self, musica):
        self.musicas.append(musica)

    def removerMusica(self, musica):
        if musica in self.musicas:  
            self.musicas.remove(musica)

    def contarMusicas(self):
        return len(self.musicas)
    
    def primeiraMusica(self):
        if self.musicas:
            print(self.musicas[0])
        else:
            print("Nenhuma musica na playlist")


    def mostrar(self):
        for i in self.musicas:
            print(i)

p1 = Playlist()
p2 = Playlist()

p1.adicionarMusica("Som a")
p1.adicionarMusica("Som b")
p1.adicionarMusica("Som c")

p2.adicionarMusica("Song x")

p1.removerMusica("Som b")  
p1.mostrar()
print(p1.contarMusicas())
p1.primeiraMusica()

p2.mostrar()
print( p2.contarMusicas())
p2.primeiraMusica()