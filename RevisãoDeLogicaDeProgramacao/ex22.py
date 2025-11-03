def contarFrequencia(frase):
   listaDePalavras = frase.lower().split()

   frequencia = {}

   for chave in listaDePalavras:
      if chave in frequencia:
         frequencia[chave]+=1
      else:
         frequencia[chave]=1

   return frequencia    


resultado = contarFrequencia("O Rato Roeu a Roupa do Rei de Roma O Rato")
print(resultado)

