Peso = float(input('Me diga seu peso ai meu bom:'))
Altura = float(input('Me diga sua altura ai meu bom:'))
IMC = Peso/(Altura*Altura)
if IMC < 18.5:
    print('Ce ta abaixo do peso meu bom!')
elif IMC > 18.5 and IMC < 25:
    print('Seu peso ta normal meu bom!')
elif IMC > 25 and IMC < 30:
    print('Ce ta acima do peso meu bom!')
else:
    print('Ce ta obeso meu bom!')