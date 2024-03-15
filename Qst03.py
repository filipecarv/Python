Dado = input('Diga quaquer coisa ai meu bom:')
if Dado.isalpha():
    print('Voce so digitou letras meu bom!')
elif Dado.isdigit():
    print('Voce so digitou numeros meu bom!')
elif Dado.isalnum():
    print('Voce digitou letras e numeros meu bom!')
else:
    print('Voce digitou so caracteres especias meu bom!')