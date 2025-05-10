# Faça um programa que leia um número inteiro qualquer
# e mostre na tela sua tabuada

print('----------------------')
print('TABUADA DE UM NÚMERO. ')
print('----------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
for contador in range (11):
    print(f'{numero} x {contador} = {numero * contador}')