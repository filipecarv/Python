Pessoas = set()
for set in range(5):
    nome = str(input('Diga seu nome meu bom:'))
    estado = str(input('Diga seu estado:'))
    Pessoas.add(nome)
    Pessoas.add(estado)
print(f'Os nomes e estados adicionados são: {Pessoas}')
Verificar1 = input('Diga o nome que voce quer verificar meu bom:')
if Verificar1 in Pessoas:
    print(f'o nome {Verificar1} esta na lista meu bom!')
else:
    print(f'O nome {Verificar1} não foi encotrado na lista meu bom!')
Verificar2 = input('Diga o estado que voce quer verificar meu bom:')
if Verificar2 in Pessoas:
    print(f'O estado {Verificar2} esta na lista meu bom!')
else:
    print(f'O estado {Verificar2} não foi encotrado na lista meu bom!')