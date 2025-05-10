# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

# Leitura de dados
while True:
    try:
        salario = float(input('Digite o valor do seu salário: R$'))
        break
    except ValueError:
        print('Por favor, digite apenas números!')

#Condicionais + Retorno de informações
if salario > 1250:
    print(f'O seu salário receberá um aumento de 10%:\033[33m R${salario * 1.1:.2f}')
else:
    print(f'O seu salário receberá um aumento de 15%:\033[33m R${salario * 1.15:.2f}')

