#Escreva um programa que peça ao usuário dois números
#e imprima se eles são iguais ou diferentes.

#Leitura de dados
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite um número: '))

#Condicional + Retorno de informações
if numero1 == numero2:
    print(f'O número {numero1} é igual ao número {numero2}.')
else:
    print(f'O número {numero1} e o {numero2} são diferentes.')