Valores = []
Pares = []
for i in range(10):
    valor = int(input('Diga um numero ai meu bom:'))
    Valores.append(valor)
    if valor % 2 == 0:
        Pares.append(valor)
print(f'Os numeros pares são: {Pares} meu bom!')