# Crie um programa que leia um nome, e mostre o primeiro e o último nome

#Leitura do nome
nome = input("Digite seu nome completo: ").strip()
print()

#Primeiro nome
primeiro_espaco = nome.find(' ') # Encontrou o primeiro espaço (esquerda p direita)
primeiro_nome = nome[ :primeiro_espaco] #Vai do ínicio até o primeiro espaço

#Último nome
ultimo_espaco = nome.rfind(' ') # Encontrou o último espaço (Direita p esquerda)
ultimo_nome = nome[ultimo_espaco + 1: ] # Vai do último espaço em diante (SOMO + 1 porque o espaço está sempre contido).

#Retorno de informações
print(f'Seu primeiro nome é: {primeiro_nome}.'
      f'\nE seu último nome é: {ultimo_nome}.')