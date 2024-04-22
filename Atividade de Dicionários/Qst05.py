while True:
    dicionario = {}
    nome = str(input('Diga seu nome ai doido:'))
    telefone = int(input('Diga seu telefone ai doido:'))
    endereço = str(input('Diga seu endereço ai doido:'))
    CEP = int(input('Diga seu CEP ai doido:'))
    dicionario[nome] = telefone
    dicionario[endereço] = CEP
    break
print('Dicionario atual:',dicionario)
verificar = str(input('Diga um nome para verificar se ja tem no dicionario:'))
if verificar in dicionario:
    print(f'O nome {verificar} ja existe no dicionario meu bom!')
else:
    telefone = int(input('Diga seu telefone ai doido:'))
    endereço = str(input('Diga seu endereço ai doido:'))
    CEP = int(input('Diga seu CEP ai doido:'))
    dicionario[verificar] = telefone
    dicionario[endereço] = CEP
    print('As novas informações foram adicionadas com sucesso meu bom!')
    print('Dicionario atualizado;',dicionario)