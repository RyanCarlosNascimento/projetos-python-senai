# Calcule a média aritimética simples, moda, mediana das seguintes notas.

#Importação da biblioteca
import statistics

#Lista com valores
notas = [5.7, 6.5, 6.9, 8.3, 8, 4.2, 6.3, 7.4, 6.9]

#Média, moda e mediana
print('Para o intervalo de valores temos as seguintes Medidas de Posição:'
      f'\nMédia: {statistics.mean(notas):.2f}'
      f'\nModa: {statistics.mode(notas):.2f}'
      f'\nMediana: {statistics.median(notas):.2f}')
