def livro(Nome, Autor, Preço, Qtd_Paginas):
    print(f'Ta ai o nome do livro meu bom: {Nome}')
    print(f'Ta ai o autor do livro meu bom: {Autor}')
    print(f'Ta ai o preço do livro meu bom: R$ {Preço}')
    print(f'Ta ai a quantidade de paginas meu bom: {Qtd_Paginas}')
def menu():
    Nome = input('Diga o nome do livro meu bom:')
    Autor = input('Diga o autor do livro meu bom:')
    Preço = float(input('Diga o preço do livro meu bom:'))
    Qtd_Paginas = int(input('Diga a quantidade de paginas meu bom:'))
    livro(Nome, Autor, Preço, Qtd_Paginas)
menu()