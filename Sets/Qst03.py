lista = {'Filipe','Alclesio','Joviara','Clemilton','Lucimara','Osvaldo'}
nome = input('Diga um nome para adicionar meu bom:')
lista.add(nome)
remover = input('Diga um nome para remover meu bom:')
lista.discard(remover)
print(lista)