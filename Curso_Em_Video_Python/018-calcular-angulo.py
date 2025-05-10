# Faça um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

print('------------------------------------')
print('CALCULO DE SENO, COSSENO E TANGENTE.')
print('------------------------------------')

#Importação da biblioteca matemática
import math

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        angulo = float(input('Digite o valor do angulo: '))
        break
    except:
        print('Por favor, digite apenas números!')

# Exibição de resultados
print(f'O valor do seno:\033[33m {math.sin(math.radians(angulo)):.2f}' #Converte de Rad para Graus e
# calcula o valor do seno do angulo.
      f'\nO valor do cosseno:\033[33m {math.cos(math.radians(angulo)):.2f}'
      f'\nO valor da tangente:\033[33m {math.tan(math.radians(angulo)):.2f}')

