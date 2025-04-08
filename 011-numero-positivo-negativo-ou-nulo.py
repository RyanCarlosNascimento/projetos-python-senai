# Escreva um programa que peça ao usuário um número
# e imprima se é positivo ou negativo.

#Leitura de dados
numero = float(input('Digite um número: '))

#Condicional + Retorno de informações
if numero > 0:
    print (f'O número {numero} é positivo.')
elif (numero == 0):
    print(f'O número {numero} é nulo ou neutro.')
else:
    print(f'O número {numero} é negativo.')
