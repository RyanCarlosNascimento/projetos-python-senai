# Encontre a posição do 70° percentil

# Importação de biblioteca(s)
from math import trunc
import numpy as np

#Lista com valores
dados = [4, 8, 6, 10, 12, 14]

#Posição terceiro quartil
pos_70_percentil = 70 / 100 * (len(dados) + 1)
if pos_70_percentil == int:
    print(f'A posição do 3° quartil é: {pos_70_percentil}')
else:
    print(f'A posição do 3° quartil está entre: {trunc(pos_70_percentil)} e {trunc(pos_70_percentil) + 1}')

# Valor do 70° quartil
print(f'70° percentil: {np.percentile(dados, 70):.2f}')
