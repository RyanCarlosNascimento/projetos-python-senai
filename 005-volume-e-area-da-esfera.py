#Escreva um programa que leia o raio de uma esfera
# e calcule o seu volume
# e área.

#Leitura de dados
print('Vamos calcular o volume e a área de uma esfera!')
print()
raio = float(input('Digite o valor do raio: '))

volume = (4/3) * 3.14 * raio ** 3
area = 4 * 3.1415 * raio ** 2

#Retorno de dados
print(f'O volume da sua esfera é: {volume:.2f} m³ '
      f'\nA área da sua esfera é: {area:.2f} m²')