from random import shuffle

primeiro_aluno = str(input('Primeiro aluno: '))
segundo_aluno = str(input('Segundo aluno: '))
terceiro_aluno = str(input('Terceiro aluno: '))
quarto_aluno = str(input('Quarto aluno: '))
lista = [primeiro_aluno, segundo_aluno, terceiro_aluno, quarto_aluno]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)