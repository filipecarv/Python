def funcionario(nome, idade, profissão):
    return nome, idade, profissão
def menu():
    nome = input('Diga seu nome meu bom:')
    idade = int(input('Diga sua idade meu bom:'))
    profissão = input('Diga sua profissão emu bom:')
    print(f'O seu nome e: {nome} meu bom!')
    print(f'A sua idade e: {idade} meu bom!')
    print(f'A sua profissão e: {profissão} meu bom!')
menu()