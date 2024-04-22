while True:
    nome = str(input('Diga seu nome meu bom:'))
    if len(nome) > 3:
        break
    else:
        print('O seu nome precisa ter mais de 3 letras digite novamente meu bom!')
while True:
    idade = int(input('Diga sua idade meu bom:'))
    if idade >= 0 and idade <= 150:
        break
    if idade < 0:
        print('Como que tu não nasceu doido!')
    else:
        print('Caramba vei como tu tem mais de 150 anos bixo me da uma dica ai doido!')
while True:
    salario = float(input('Diga seu salario meu bom:'))
    if salario >= 0:
        break
    else:
        print('Tas devendo muito ne bixo!')
print(f'Que nome lindo voce tem viu {nome}!')
print(f'Voce so tem {idade} anos ta jovem demais ainda doido!')
print(f'Voce ganha {salario}, tas rico visse doido!')