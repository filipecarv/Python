Valores = []
for i in range(4):
    valor = input(f'Diga um numero meu bom:')
    Valores.append(valor)
remover = Valores.pop()
print(f'Voce removeu {remover} de valores meu bom!')
Valores.clear()
print(f'A lista certa e {Valores} meu bom!')