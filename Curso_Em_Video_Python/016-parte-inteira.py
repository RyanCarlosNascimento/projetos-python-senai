# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção Inteira.

#Importação da função 'trunc' da biblioteca 'math'
from math import trunc

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        numero = float(input('Digite um número qualquer: '))
        break
    except:
        print('Por favor, digite apenas números!')

# Exibição de resultados
print(f'A parte inteira do número digitado é:\033[33m {trunc(numero)}')

# Outra resolução
print(f'A parte inteira do número digitado é:\033[33m {int(numero)}')


