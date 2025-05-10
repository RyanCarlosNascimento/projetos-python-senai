# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar $1 = R$6

print('-----------------------------')
print('COMPRA DE DÓLARES COM REAIS. ')
print('-----------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        carteira = int(input('Quanto você tem na carteira nesse momento?: R$ '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'Você pode comprar \033[33m${carteira / 6:.2f}\033[m com \033[33mR${carteira}\033[m')