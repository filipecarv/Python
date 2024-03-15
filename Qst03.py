lista = []
dicionario = {}
nome = str(input('Diga seu nome ai doido:'))
idade = int(input('Diga sua idade ai doido:'))
dicionario[nome] = idade
lista.append(dicionario.copy())
print('Ta ai a lista com as chaves do dicionario doido:',lista)