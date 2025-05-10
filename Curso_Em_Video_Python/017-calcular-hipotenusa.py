# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

import math

print('-----------------------------')
print('   CÁLCULO DA HIPOTENUSA.    ')
print('-----------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        cateto_oposto = float(input('Digite o valor do cateto oposto: '))
        cateto_adjacente = float(input('Digite o valor do cateto adjacente: '))
        break
    except:
        print('Por favor, digite apenas números.')

# Exibição de resultados
print(f'A hipotenusa desse triângulo retângulo é:\033[33m {math.hypot(cateto_adjacente, cateto_oposto):.2f}')

#Outra resolução -> c² = a² + b² --> c= √a² + b²
hipotenusa = math.sqrt(cateto_oposto ** 2 + cateto_adjacente ** 2)
print(f'A hipotenusa desse triângulo retângulo é:\033[33m {hipotenusa:.2f}')
