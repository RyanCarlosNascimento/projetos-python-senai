# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.

print('--------------------------')
print('Calcule de média do aluno!')
print('--------------------------')

# Declaração da variável global 'soma'
soma = 0

# Leitura de dados + Verificação de possíveis erros
for _ in range (2):
    while True:
        try:
            nota = float(input('Digite a nota do aluno: '))
            soma = + nota / 2
            break
        except ValueError:
            print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'A média do(a) aluno(a) é:\033[33m {soma}')