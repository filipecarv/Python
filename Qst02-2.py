from Qst02 import Aluno
nome = input('Diga seu nome meu bom:')
nmr_matricula = input('Diga o seu numero da matricula meu bom:')
curso = input('Diga seu curso meu bom:')
objeto = Aluno(nome,nmr_matricula,curso)
objeto.mostar_curso(curso)
alterar = int(input('Voce deseja alterar o curso! \n[1]Sim\n[2]Não\nQual opção voce deseja:'))
if alterar == 1:
    novo_curso = input('Diga seu novo curso meu bom:')
    print('Seu curso foi alterado com sucesso seu novo curso e:',novo_curso)
elif alterar ==2:
    print('Obrigado!')
else:
    print('v0#1 B$@%¨!&Ou 0 C*!@%&O')