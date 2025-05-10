# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

#Variaveis globais
maior_numero = None
menor_numero = None

#Estrutura de repetição
for _ in range (3):
    numero = float(input('Digite um número: '))

    #Atribuição de valor inicial para ambas as categorias
    if maior_numero == None and menor_numero == None:
        maior_numero = numero
        menor_numero = numero

    #Maior peso
    if numero > maior_numero:
        maior_numero = numero

    #Menor peso
    elif menor_numero > numero:
        menor_numero = numero

# Exibição de resultados
print(f'O maior número digitado foi:\033[33m {maior_numero} \033[m'
      f'\nE o menos número foi:\033[33m {menor_numero} \033[m')