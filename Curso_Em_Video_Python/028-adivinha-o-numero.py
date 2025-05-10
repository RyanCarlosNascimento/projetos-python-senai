# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

# Importação de biblioteca
import time
import random
pc = random.randint(0, 5)

# Leitura de dados
jogador = int(input('Digite um número entre 1 e 5 para adivinhar a jogada do computador: '))

time.sleep(1)
print('Hummmm...')
time.sleep(1)
print('O computador está pensando...')
time.sleep(1)
print(f'O computador jogou {pc}')
time.sleep(1)

# Condicional + Exibição de resultados
if jogador == pc:
    print('\033[32mParabéns você acertou!')
else:
    print('\033[31mInfelizmente você errou!')


