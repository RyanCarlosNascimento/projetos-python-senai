# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 1° O nome com todas as letras maiúsculas e minúsculas.
# 2° Quantas letras ao todo (sem considerar espaços).
# 3° Quantas letras tem o primeiro nome.

# Leitura de dados + Verificação de possíveis erros
while True:
    nome = input('Digite o seu nome completo: ').strip()
    if nome.replace(' ', '').isalpha():
        break
    print('Por favor! Digite apenas letras!')

#2°
quantidade_letras_nome = len(nome.replace(' ', ''))

#3°
primeiro_espaco = nome.find(' ')
quantidade_letras_primeiro_nome = len(nome[:primeiro_espaco])


# Exibição de resultados
print(f'O nome com APENAS maiúsculas:\033[33m {nome.upper()}. \033[m'
      f'\nO nome com APENAS minúsculas:\033[33m {nome.lower()}. \033[m'
      f'\nO nome tem ao todo:\033[33m {quantidade_letras_nome} letras. \033[m'
      f'\nO primeiro nome tem ao todo:\033[33m {quantidade_letras_primeiro_nome} letras. \033[m')