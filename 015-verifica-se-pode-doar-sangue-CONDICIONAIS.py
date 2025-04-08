#Crie um programa que verifica se uma pessoa pode ser doadora de sangue,
# 1. considerando a idade e CINCO critérios de saúde.

# 1° Condicional - Idade + Leitura de dados + Retorno de informações
idade = int(input('Digite a sua idade: '))

peso = float(input('Digite o seu peso: '))

se_beber = input('Você bebe? (Sim/Não): ').strip().upper()
se_beber = se_beber.replace('Ã', 'A')

se_tem_tatuagem = input('Você tem tatuagem? (Sim/Não): ').strip().upper()
se_tem_tatuagem = se_tem_tatuagem.replace('Ã', 'A')

se_fumar =input('Você fuma? (Sim/Não): ').strip().upper()
se_fumar = se_fumar.replace('Ã', 'A')

if (16 <= idade <= 69) and (peso >= 50) and (se_beber == 'NAO') and (se_tem_tatuagem == 'NAO') and (se_fumar == 'NAO'):
    print('Parabéns, você atende a todos os critérios para doar sangue.')
elif (se_beber == 'SIM') or (se_tem_tatuagem == 'SIM') or (se_fumar == 'SIM'):
    print('Precisamos verificar outros critérios antes de CONFIRMAR a sua doação de sangue.'
    '\n Por favor, responda a mais alguma(s) pergunta(s).')
    print()
else:
    print('Que pena, você NÃO atende aos critérios para doar sangue.')

if (se_beber == 'SIM'):
    horas_bebida = float(input('Quantas horas faz desde a última vez que você consumiu bebida alcoólica? '))
    if horas_bebida < 12:
        print('Reprovado no critério de bebida alcólica! Não pode ser um doador de sangue, então encerramos por aqui.')
        exit()

if (se_tem_tatuagem == 'SIM'):
    dias_tatuagem = float(input('Quantos dias faz desde a sua última tatuagem? '))
    if dias_tatuagem < 183:
        print('Reprovado no critério de tatuagem! Não pode ser um doador de sangue, então encerramos por aqui.')
        exit()
if (se_fumar == 'SIM'):
    horas_fumo = float(input('Quantas horas faz desde a última vez que você fumou? '))
    if horas_fumo < 2:
        print('Reprovado no critério de fumar! Não pode ser um doador de sangue, então encerramos por aqui.')
        exit()
    else:
        print('Aprovado, no(s) critério(s) restante(s)! Pode OFICIALMENTE ser um doador de sangue.')
