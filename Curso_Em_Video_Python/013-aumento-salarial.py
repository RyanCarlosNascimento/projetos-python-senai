# Faça um algoritmo que leia o salário de um funcionário
# e mostre seu novo salário com 15% de aumento.

print('-----------------------------')
print('CALCULO DE AUMENTO SALÁRIAL. ')
print('-----------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        salario = float(input('Qual o valor seu salário: R$ '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'O novo salário deste(a) funcionário(a) com um aumento de 15% é:\033[33m R${salario * 1.15:.2f}')