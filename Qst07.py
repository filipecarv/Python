while True:
    Calculadora = int(input('Bem-Vindo(a) a Calculadora! \n [1] Somar \n [2] Subtrair \n [3] Sair \n Qual opção voce deseja:'))
    if Calculadora == 1:
        while True:
            N1 = float(input('Diga o primeiro numero meu bom:'))
            N2 = float(input('Diga o segundo numero meu bom:'))
            soma = N1 + N2
            print('Deu',soma)
            Calculadora = int(input('Voce quer continuar ou sair! \n [1] Continuar \n [2] Sair \n Qual opção voce deseja:'))
            if Calculadora == 1:
                print('Aguarde alguns segundos meu bom!')
            elif Calculadora == 2:
                print('Aguarde alguns segundos meu bom!')
                break
            else:
                print('V@c! d!@it$& @m n@m#r& in@#l%@$do qu@#! t@#ou o si@#$@MA te%@@t$ n%$@&t% m@7s t@%&#D3 M3& @O#!')
                break
    elif Calculadora == 2:
        while True:
            N1 = float(input('Diga o primeiro numero meu bom:'))
            N2 = float(input('Diga o segundo numero meu bom:'))
            subtração = N1 - N2
            print('Deu',subtração)
            Calculadora = int(input('Voce quer continuar ou sair! \n [1] Continuar \n [2] Sair \n Qual opçao voce deseja:'))
            if Calculadora == 1:
                print('Aguarde alguns segundos meu bom!')
            elif Calculadora == 2:
                print('Aguarde alguns segundos meu bom!')
                break
            else:
                print('V@c! d!@it$& @m n@m#r& in@#l%@$do qu@#! t@#ou o si@#$@MA te%@@t$ n%$@&t% m@7s t@%&#D3 M3& @O#!')
                break
    elif Calculadora == 3:
        print('Obrigado e volte sempre meu bom!')
        break
    else:
        print('V@c! d!@it$& @m n@m#r& in@#l%@$do qu@#! t@#ou o si@#$@MA te%@@t$ n%$@&t% m@7s t@%&#D3 M3& @O#!')
        break