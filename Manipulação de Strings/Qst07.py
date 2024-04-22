frase = input('Diga alguma frase meu bom:')
nome = input('Diga o nome que voce deseja verificar:')
if nome in frase:
    print(f'{nome} esta na frase!')
else:
    print(f'{nome} não esta na frase!')