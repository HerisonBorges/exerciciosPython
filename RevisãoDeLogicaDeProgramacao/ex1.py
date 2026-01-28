def verificarPessoa(usuario):
    
    if usuario["autorizado"] == True:
        
        return f"Acesso permitido para {usuario['nome']}"
    else:
        return "Acesso negado!"

pessoa1 = {}

pessoa1["nome"] = input("Informe o nome: ")
pessoa1["autorizado"] = True 

verificar = verificarPessoa(pessoa1)
print(verificar)