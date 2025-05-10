# Escreva um programa que leia um valor em metros
# e o exiba convertido em centímetros e milímetros.

print('---------------------------------------------------')
print('Conversor de METROS para CENTÍMETROS E MILÍMETROS. ')
print('-------------------------------------------------- ')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        numero = float(input('Digite um número: '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'Em centímetros:\033[33m {numero * 100:.2f} cm\033[m' # Deixar apenas com duas casas depois da virgula.
      f'\nEm milímetros:\033[33m {numero * 1000:.2f} mm\033[m')