from Qst01 import Funcionario
nome = input('Diga seu nome meu bom:')
salario = input('Diga seu salario:')
objeto = Funcionario(nome,salario)
objeto.mostrar_nome(nome)
objeto.mostrar_salario(salario)