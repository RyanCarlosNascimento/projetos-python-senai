# Identifique a Assimetria:

# Importação de bibliotecas
import statistics

def assimetria(x):
    #Média
    media = statistics.mean(x)

    #Moda
    moda = statistics.mode(x)

    #Desvio Padrão
    desvio_padrao = statistics.stdev(x)

    #Assimetria Calculo
    assimetria_pearson = (media - moda) / desvio_padrao
    print(f'O valor da assimetria é: {assimetria_pearson:.2f}')

    #Tipo de assimetria
    if assimetria_pearson == 0:
        print('Temos uma distribuição simétrica!')
    elif assimetria_pearson > 0:
        print('Assimetria positiva! Cauda a direita.')
    else:
        print('Assimetria negativa! Cauda a esquerda.')

#Lista com valores
desvio = [3, 3, 4, 4, 5, 6, 7, 9, 12, 20]
desvio_1 = [4, 5, 5, 5, 6, 7, 7, 10, 12, 15]


assimetria(desvio)
print('---------------------------')
assimetria(desvio_1)
