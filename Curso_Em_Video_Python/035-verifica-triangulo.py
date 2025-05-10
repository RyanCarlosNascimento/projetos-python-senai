# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

# Leitura de dados
while True:
    try:
        reta1 = float(input('Digite o comprimento da reta (cm): '))
        reta2 = float(input('Digite o comprimento da reta (cm): '))
        reta3 = float(input('Digite o comprimento da reta (cm): '))
        break
    except ValueError:
        print('Por favor, digite apenas números!')

#Condicionais + Retorno de informações
if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    print('\033[32mÉ possível formar um triângulo!')
else:
    print('\033[31mNÃO é possível formar um triângulo!')


