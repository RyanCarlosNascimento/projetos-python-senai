#Escreva um programa que execute o cálculo da Função horária da posição no MRUV,
# e retorne de acordo com o tempo informado pelo usuário

#Leitura de dados
print('vamos calcular a posição S com base na Função horária do MRUV!')
print()
espaco_inicial = float(input('Digite o valor do So (Espaço inicial): '))
velocidade_inicial = float(input('Digite o valor do Vo (Velocidade inicial): '))
aceleracao = float(input('Digite o valor do a (aceleração): '))
tempo = float(input('Digite o valor do t (tempo): '))

#Dados aplicados na fórmula.
espaco_final = espaco_inicial + velocidade_inicial * tempo + (aceleracao * (tempo ** 2)) / 2

#Retorno de informações
print(f'O valor de S (Espaço) da função horária do MRUV é: {espaco_final:.2f} m no tempo {tempo} s.')
