class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
nome = input('Diga seu nome meu bom:')
idade = int(input('Diga sua idade meu bom:'))
altura = float(input('Diga sua altura meu bom:'))
peso = float(input('Diga seu peso meu bom:'))
pessoa = Pessoa(nome, idade, altura, peso)
print(f'Seu nome e: {pessoa.nome} que legal!')
print(f'Sua idade e: {pessoa.idade} que legal!')
print(f'Sua altura e: {pessoa.altura} que legal!')
print(f'Seu peso e: {pessoa.peso} que legal!')