# Procure o Terceiro Quartil:

# Importação de biblioteca(s)
from math import trunc
import numpy as np

#Lista com valores
dados = [12, 15, 14, 10, 18, 20, 22, 17, 19, 16]

#Posição terceiro quartil
pos_3q = 75 / 100 * (len(dados) + 1)
if pos_3q == int:
    print(f'A posição do 3° quartil é: {pos_3q}')
else:
    print(f'A posição do 3° quartil está entre: {trunc(pos_3q)} e {trunc(pos_3q) + 1}')

#Valor do 3° quartil
    print(f'3° Quartil: {np.percentile(dados, 75):.2f}')
