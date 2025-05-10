# Exercício Python 24: Crie um programa que leia o nome de uma cidade
# diga se ela começa ou não com o nome “SANTO”.

# Leitura de dados + Verificação de possíveis erros
cidade = input('Digite o nome de uma cidade: ').strip().upper()

# Condicional + Exibição de resultados
if cidade.split()[0] == 'SANTO':
    print('\033[32mO nome da sua cidade começa com a palavra "Santo". ')
else:
    print('\033[31mO nome da sua cidade NÃO começa com a palavra "Santo". ')


