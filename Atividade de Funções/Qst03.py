def alterar_nome(nomeAtual):
    Novo_nome = input('Diga seu novo nome meu bom:')
    return Novo_nome
def alterar_matricula(matriculaAtual):
    Nova_matricula = input('Diga sua nova matricula meu bom:')
    return Nova_matricula
nome = input('Diga seu nome meu bom:')
matricula = input('Diga sua matricula meu bom:')
print(f'Nome: {nome}')
print(f'Matricula: {matricula}')
alterar = input('Deseja alterar alguma coisa meu bom:')
if alterar.upper() == 'S':
    alterarDado = input('O que voce deseja alterar meu bom:')
    if alterarDado.upper() == 'N':
        nome = alterar_nome(nome)
        print(f'Seu novo nome e: {nome}')
    elif alterarDado.upper() == 'M':
        matricula = alterar_matricula(matricula)
        print(f'Sua nova matricula e {matricula}')
    else:
        print('V@c! d!@it$& @m4 &3tR4 in@#l%@$d4 qu@#! t@#ou o si@#$@MA te%@@t$ n%$@&t% m@7s t@%&#D3 M3& @O#!')
else:
    print('Voce não alterou nehum dado meu bom!')