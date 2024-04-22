Inteiro = int(input('Diga um número inteiro ai:'))
Decimal = float(input('Diga um número decimal ai:'))
Texto = str(input('Diga um texto ai:'))
Decimal_Inteiro = float(Inteiro)
Texto_Decimal = str(Decimal)
if Texto.isnumeric():
    Texto_Inteiro = int(Texto)
else:
    Texto_Inteiro = None
print('O número inteiro em decimal é:', Decimal_Inteiro, 'do tipo:', type(Decimal_Inteiro))
print('O número decimal em texto é:', Texto_Decimal, 'do tipo:', type(Texto_Decimal))
if Texto_Inteiro is not None:
    print('O texto em inteiro é:', Texto_Inteiro, 'do tipo:', type(Texto_Inteiro))
else:
    print('Não deu para converter o texto em inteiro!')