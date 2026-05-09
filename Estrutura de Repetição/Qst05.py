while True:
    Nome = input('Diga seu nome de usuario meu bom:')
    Senha = input('Diga sua senha meu bom:')
    if Senha != Nome:
        print(f'Seja Bem-Vindo(a) Sr(a).{Nome}!')
        break
    else:
        print('Algo de errado não esta certo tente novamente meu bom!')