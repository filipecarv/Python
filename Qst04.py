class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.estado = 'Saudável'
    def correr(self):
        print(f'{self.nome} prefere correr!')
        self.estado = 'Cansado'  
    def comer(self):
        print(f'{self.nome} prefere comer!')
        self.estado = 'Satisfeito' 
    def dormir(self):
        print(f'{self.nome} prefere dormir!')
        self.estado = 'Descansado'
    def mostrar(self, opcao):
        if opcao == 1:
            self.correr()
        elif opcao == 2:
            self.comer()
        elif opcao == 3:
            self.dormir()
        else:
            print('v0#1 B$@%¨!&Ou 0 C*!@%&O')
        return f'Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura}, Peso: {self.peso}, Estado: {self.estado}'
nome = input('Diga seu nome meu bom:')
idade = int(input('Diga sua idade meu bom:'))
altura = float(input('Diga sua altura meu bom:'))
peso = float(input('Diga seu peso meu bom:'))
p = Pessoa(nome, idade, altura, peso)
print(p.mostrar(1))
print(p.mostrar(2))
print(p.mostrar(3))
print(p.mostrar(4))