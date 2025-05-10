# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela
# o nome do escolhido.

#Importação de biblioteca
import random

#Leitura de dados
while True:
    n1 = input('Digite o nome do 1° aluno: ').strip().capitalize()
    n2 = input('Digite o nome do 2° aluno: ').strip().capitalize()
    n3 = input('Digite o nome do 3° aluno: ').strip().capitalize()
    n4 = input('Digite o nome do 4° aluno: ').strip().capitalize()

# Exibição de resultados
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista) #Randomiza os valores mostrados na lista.
print(f'O aluno escolhido foi:\033[33m {escolhido}')
