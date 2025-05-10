# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Leitura de dados
numero = input('Digite um número entre 0 a 9999: ')

if len(numero) == 1: # Se a quantidade de letras da string for 1
    print(numero[0]) # Mostra o número na posição 0

elif len(numero) == 2: # Se a quantidade de letras da string for 2
    print(numero[0]) # Mostra o número na posição 0
    print(numero[1]) # E o número na posição 1

elif len(numero) == 3:  # Se a quantidade de letras da string for 3
    print(numero[0]) # Mostra o número na posição 0
    print(numero[1]) # E o número na posição 1
    print(numero[2]) # E o número na posição 2

elif len(numero) == 4:
    print(numero[0]) # Mostra o número na posição 0
    print(numero[1]) # E o número na posição 1
    print(numero[2]) # E o número na posição 2
    print(numero[3]) # E o número na posição 3
