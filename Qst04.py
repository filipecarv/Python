while True:
    Nota = float(input('Diga sua nota meu bom:'))
    if Nota >= 0 and Nota <= 10:
        print(f'Sua nota foi: {Nota} meu bom!')
        break
    else:
        print('A nota que voce digitou deu erro meu bom digite novamente!')