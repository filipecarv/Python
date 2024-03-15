class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario
    def mostrar_nome(self,nome):
        print('Teu nome e:', nome)
    def mostrar_salario(self,salario):
        print('Teu salario e:', salario)