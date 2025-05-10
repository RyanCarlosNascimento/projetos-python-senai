# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

# Leitura de dados
nome = input('Digite o seu nome completo: ').strip().title()

# Exibição de resultados
print(f'O seu primeiro nome é:\033[33m {nome.split()[0]} \033[m'
      f'\nO seu último nome é:\033[33m {nome.split()[-1]} \033[m')