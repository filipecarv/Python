try:
    N1 = int(input('Diga um numero ai doido:'))
    N2 = int(input('Diga outro numero ai doido:'))
    Divisão = N1 / N2
except ZeroDivisionError:
    print('Voce não pode dividir um numero por zero meu bom!')
else:
    print(f'Deu: {Divisão} meu bom!')
finally:
    print('O programa foi encerrado com sucesso meu bom!')  