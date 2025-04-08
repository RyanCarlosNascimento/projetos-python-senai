#Crie um programa para analisar o IMC de uma pessoa,
# e classifique se ela está entre a faixa ideal, acima ou abaixo do IMC ideal.

#Leitura de dados
peso = float(input('Digite o seu peso (kg): '))
altura = float(input('Digite a sua altura (m): '))

#Calculo IMC
IMC = peso / (altura ** 2)

#Condicionais + Retorno de informações
if IMC < 18.5:
    print ('Você está abaixo do peso!')
elif (18.5 <= IMC <= 24.9):
    print('Você está no peso adequado!')
elif (25 <= IMC <= 29.9 ):
    print('Sobrepeso!')
elif (30 <= IMC <= 34.9):
    print('Você está com OBESDIDADE I GRAU!!')
elif (35 <= IMC <= 39.9):
    print('Você está com OBESDIDADE II GRAU!!')
else:
    print('Você está com OBESDIDADE III GRAU!!')