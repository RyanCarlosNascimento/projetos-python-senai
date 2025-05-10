# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print('-----------------------------')
print('     ALUGUEL DE CARROS.      ')
print('-----------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        dias_alugados = float(input('Digite a quantidade de dias que o carro ficou alugado: '))
        km_percorridos = float(input('Digite a quantidade de KMs percorridos com o carro: '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'O preço final a pagar pelo aluguel é:\033[33m R${(dias_alugados * 60) + (km_percorridos * 0.15):.2f}')