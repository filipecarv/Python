def info (Nome, Telefone):
    return Nome, Telefone
def menu():
    Nome = str(input('Diga seu nome meu bom:'))
    Telefone = int(input('Diga seu telefone meu bom:'))
    return Nome, Telefone
menu()