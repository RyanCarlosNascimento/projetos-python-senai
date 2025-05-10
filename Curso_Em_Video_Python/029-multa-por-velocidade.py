# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

# Leitura de dados
while True:
    try:
        velocidade = float(input('Digite a velocidade que o carro passou no radar (km/h): '))
        break
    except ValueError:
        print('Por favor, digite apenas números!')

# Condicional + Exibição de resultados
if velocidade > 80:
    print(f'\033[31mVocê está acima do limite de velocidade!'
          f'\nO valor da multa será de R${(velocidade-80) * 7}')
else:
    print('\033[32mVocê está dentro do limite de velocidade')