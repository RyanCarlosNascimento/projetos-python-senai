# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))

if n1 > n2:
    print(f'{n1} é maior que {n2} - Portanto, o primeiro valor é maior')
elif n2 > n1:
    print(f'{n2} é maior que {n1} - Portanto, o segundo valor é maior')
else:
    print(f'{n1} é igual a {n2}')

