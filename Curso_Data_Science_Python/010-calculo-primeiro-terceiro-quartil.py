# Calcule o primeiro e o terceiro quartis:


# Importação de biblioteca(s)
import statistics
import numpy as np #Biblioteca para calculo do percentil direto.

#Lista com valores
quartis = [12, 15, 14, 10, 18, 20, 22, 17, 19, 16, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

# Quartis
print(f'1° Quartil: {np.percentile(quartis, 25):.2f}'
      f'\n3° Quartil: {np.percentile(quartis, 75):.2f}')
