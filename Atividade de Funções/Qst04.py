def soma(N1, N2):
    return N1 + N2
def sub(N1, N2):
    return N1 - N2
def principal():
    N1 = float(input('Diga um numero ai meu bom:'))
    N2 = float(input('Diga outro numero ai meu bom:'))
    result_soma = soma(N1, N2)
    result_sub = sub(N1, N2)
    print(f'A soma deu: {result_soma} meu bom!')
    print(f'A subtração deu: {result_sub} meu bom!')
principal()