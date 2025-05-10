# Crie um script em Python que leia o dia, mês e ano de nascimento de uma pessoa
# e mostre uma mensagem com a data formatada.

#Leitura de dados + Verificação de possíveis erros
print('-------------------')
while True:
    try:
        dia = int(input('Digite o dia: '))
        mes = int(input('Digite o mês: '))
        ano = int(input('Digite o ano: '))
        break
    except ValueError:  # Nesse caso se não digitar valores inteiros, pede-se ao usuário que digite de novo.
        print('Valor inválido! Digite apenas números inteiros.')
print('-------------------')

# Exibição de resultados
print(f'A data digitada foi:\033[33m {dia}/{mes}/{ano}')