#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1. O nome com todas as letras maiúsculas
#2. O nome com todas minúsculas
#3. Quantas letras ao todo (sem considerar os espaços)
#4. Quantas letras tem o primeiro nome

#Leitura de dados
nome = input("Digite seu nome completo: ").strip()
print()

#3.1
total_letras = len(nome) # Conta quantos CARACTERES (Espaços e letras) tem no nome no TOTAL
total_espaco = nome.count(" ") # Conta a quantidade de espaços
total_letras_sem_espaco_v1 = total_letras - total_espaco # Subtrai o total de carácteres - total de espaços.

#3.2
nome_sem_espacos = nome.replace(' ', '') # Substitui os espaços por vazio - A palavra fica TODAJUNTA
total_letras_sem_espaco_v2 = len(nome_sem_espacos) # Conta a quantidade de letras do nome já sem espaços.

#4.1
posicao_espaco = nome.find(' ') # Encontra a posição do primeiro espaço
quantidade_letras_primeiro_nome_v1 = nome[:posicao_espaco] # Com fatiamento, conta do inicio '' ou 0 até o primeiro espaço

#4.2
quantidade_letras_primeiro_nome_v2 = nome.find(' ') #Começando da esquerda para direita, até o primeiro espaço acontecerá uma contagem de letras.
#Vale lembrar que aqui, já é um número inteiro, então não preciso usar LEN no print

#Retorno de informações
print(f'O nome com letras maiúsculas: {nome.upper()}'
      f'\n O nome com letras minúsculas: {nome.lower()}'
      f'\n A quantidade de letras sem espaço V1: {total_letras_sem_espaco_v1}'
      f'\n A quantidade de letras sem espaço V2: {total_letras_sem_espaco_v2}'
      f'\n A quantidade de letras no primeiro nome V1: {len(quantidade_letras_primeiro_nome_v1)}'
      f'\n A quantidade de letras no primeiro nome V2: {(quantidade_letras_primeiro_nome_v2)}')