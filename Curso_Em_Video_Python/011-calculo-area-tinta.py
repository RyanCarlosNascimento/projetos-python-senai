# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e quantidade de tinta necessária para pintá-la, sabendo que
# cada litro de tinta pinta uma área de 2m².

print('--------------------------------------------------')
print('CALCULO DE ÁREA E QUANTIDADE DE TINTA NECESSÁRIA. ')
print('--------------------------------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        largura = float(input('Qual a largura em metros: '))
        altura = float(input('Qual a altura em metros: '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'Para pintar uma área de\033[33m {largura * altura:.2f} m²\033[m será preciso\033[33m {(largura * altura) / 2:.2f} l\033[m de tinta. ')
