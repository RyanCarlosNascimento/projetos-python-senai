# Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.


print('-----------------------------')
print('CONVERSOR DE TEMPERATURA. ')
print('-----------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        temperatura = float(input('Digite o valor em °C: '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'A temperatura convertida é:\033[33m {(temperatura * 1.8) + 32}°F')