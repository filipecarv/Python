lista = ['Negão',99,'Chupacabra',22,'Tabacudo',13]
opção = input('[1] Texto \n[2] Numero \nQual opção voce deseja:')
if opção == '1':
    texto = input('Diga o texto que voce procura meu bom:')
    if texto in lista:
        print(f'O texto {texto} esta na lista meu bom')
    else:
        print(f'O texto {texto} não esta na lista meu bom')      
elif opção == '2':
    try:
        num = int(input('Diga o numero que voce procura meu bom:'))
        if num in lista:
            print(f'O numero {num} esta na lista meu bom!')
        else:
            print(f'O numero {num} não esta na lista meu bom!')
    except ValueError:
        print('V@c! d!@it$& @m n@m#r& in@#l%@$do qu@#! t@#ou o si@#$@MA te%@@t$ n%$@&t% m@7s t@%&#D3 M3& @O#!')     
else:
    print('V@c! d!@it$& @m n@m#r& in@#l%@$do qu@#! t@#ou o si@#$@MA te%@@t$ n%$@&t% m@7s t@%&#D3 M3& @O#!')