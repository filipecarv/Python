class Aluno:
    def __init__(self,nome,nmr_matricula,curso):
        self.nome = nome
        self.nmr_matricula = nmr_matricula
        self.curso = curso
    def mostar_curso(self,curso):
        print('Teu curso e:', curso)
    def alterar_curso(self,novo_curso):
        self.curso = novo_curso