# Calcule a Amplitude:

#Importação de biblioteca(s)
import statistics

#Criação da função para calculo da amplitude
def amplitude(x):
    #Valor Máximo
    val_max = max(x)

    #Valor Mínimo
    val_min = min(x)

    #Calculo da amplitude
    amplitude = val_max - val_min
    print(f"Amplitude: {amplitude:.2f}")

dados = [1, 2, 2, 3, 4, 5, 5, 6, 7, 8]

amplitude(dados)
