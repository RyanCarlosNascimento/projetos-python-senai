#Crie um programa para jogar JOKEMPO, usando a função random.randint

#Introdução ao usuário sobre o jogo
print('Vamos jogar JOKENPO!'
      '\n ESCOLHA [1] PEDRA'
      '\n ESCOLHA [2] PAPEL'
      '\n ESCOLHA [3] TESOURA')

# Entrada do jogador
jogador = int(input('Digite um número/opção entre 1, 2 ou 3: '))

#Sorteio do computador
import random
pc = random.randint(1,3)

# 1. Condicional - Exibe a jogada do computador com base no número sorteado (1 = Pedra, 2 = Papel, 3 = Tesoura)
if pc == 1:
    print(f'O computador jogou [{pc}] - PEDRA')
elif pc == 2:
    print(f'O computador jogou [{pc}] - PAPEL')
else:
    print(f'O computador jogou [{pc}] - TESOURA')
    
# 2. Condicional - Determina o resultado da partida comparando as escolhas do jogador e do computador
if (pc == jogador):
    print('Temos um EMPATE! Ambos escolheram a mesma opção')
elif (pc == 1) and (jogador == 2):
    print('Parabéns, o jogador venceu a PEDRA usando PAPEL!')
elif (pc == 2) and (jogador == 3):
    print('Parabéns, o jogador venceu o PAPEL usando TESOURA!')
elif (pc == 3) and (jogador == 1):
    print('Parabéns, o jogador venceu a TESOURA usando PEDRA!')
elif (jogador == 1) and (pc == 2):
    print('Infelizmente, o jogador perdeu! O computador venceu PEDRA usando PAPEL! ')
elif (jogador == 2) and (pc == 3):
    print('Infelizmente, o jogador perdeu! O computador venceu PAPEL usando TESOURA!')
else:
    print('Infelizmente, o jogador perdeu!  O computador venceu TESOURA usando PEDRA!')



