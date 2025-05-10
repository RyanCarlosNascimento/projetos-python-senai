# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

# Importação da biblioteca Random
from random import shuffle

nome1 = input('Dite o nome 1° aluno: ').strip().capitalize()
nome2 = input('Dite o nome 2° aluno: ').strip().capitalize()
nome3 = input('Dite o nome 3° aluno: ').strip().capitalize()
nome4 = input('Dite o nome 4° aluno: ').strip().capitalize()

# Definição da lista + mudança de ordem dela
lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

# Exibição de resultados
print(f'A ordem embaralhada será:\033[33m {lista}')


