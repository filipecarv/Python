lista = []
for i in range(10):
    Num = int(input('Diga um numero ai doido:'))
    lista.append(Num)
Crescente = sorted(lista)
Decrescente = sorted(lista, reverse=True)
print(f'Os numeros em ordem crescente são: {Crescente} meu bom!')
print(f'Os numeros em ordem decrescente são: {Decrescente} meu bom!')