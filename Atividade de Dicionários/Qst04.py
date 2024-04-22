dicionario = {'Chave1':22,'Chave2':13,'Chave3':99,'Chave4':69,'Chave5':157}
Valor = int(input('Diga um valor ai meu bom:'))
if Valor in dicionario.values():
    print('O valor {} esta em dicionario meu bom!'.format(Valor))
else:
    print('O valor {} não esta em dicionario meu bom!'.format(Valor))