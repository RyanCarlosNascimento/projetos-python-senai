# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

# Leitura de dados
while True:
    try:
        viagem = float(input('Digite a distância da viagem (km): '))
        break
    except ValueError:
        print('Por favor, digite apenas números!')

# Condicional + Exibição de resultados
if viagem <= 200:
    print(f'O preço da passagem é:\033[33m R$ {viagem * 0.50}')
else:
    print(f'O preço da passagem é:\033[33m R$ {viagem * 0.45}')
