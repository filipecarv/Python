lista = []
N1 = int(input('Diga um numero meu bom:'))
N2 = int(input('Diga outro numero meu bom:'))
lista.append (N1)
lista.append (N2)
if N1 > N2:
    print('O primeiro numero e maior que o segundo meu bom!')
elif N2 > N1:
    print('O segundo numero e maior que o primeiro meu bom!')
else:
    print('Os numeros sao iguais meu bom!')