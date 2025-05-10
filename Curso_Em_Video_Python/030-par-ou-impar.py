# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

# Leitura de dados
while True:
    try:
        numero = int(input('Digite um número: '))
        break
    except ValueError:
        print('Por favor, digite apenas números inteiros!')

# Condicional + Exibição de resultados
if ((numero % 2) == 0):
    print('O número\033[33m é par! \033[33m')
else:
    print('O número\033[33m é ímpar! \033[33m')



