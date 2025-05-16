# Calcule o desvio padrão:

#Importação da biblioteca
import statistics

#Lista com valores
desvio = [12, 15, 14, 10, 18, 20, 22, 17, 19, 16]

# Calcular o desvio padrão
desvio_padrao = statistics.stdev(desvio)
print(f"Desvio Padrão: {desvio_padrao:.2f}")