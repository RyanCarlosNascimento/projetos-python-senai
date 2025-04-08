#Escreva um programa que peça ao usuário um número
#e imprima se é par ou ímpar

#Leitura de dados
numero = int(input('Digite um número: '))

#Condicional + Retorno de informações
if (numero % 2) == 0: #Se o resto da divisão por dois for igual a 0
    print (f'O número {numero} é par.')
else:
    print (f'O número {numero} é ímpar.')

