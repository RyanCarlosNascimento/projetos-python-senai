# Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

# Leitura de dados
nome = input('Digite o seu nome completo: ').strip().upper()

# Condicional + Exibição de resultados
if 'SILVA' in nome:
    print('\033[32mO seu nome tem SILVA!')
else:
    print('\033[31mO seu nome NÃO tem SILVA!')
