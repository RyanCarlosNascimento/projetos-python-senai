# Faça um programa que leia um número inteiro
# e mostre na tela o seu sucessor e seu antecessor.

#Apresentação do programa ao usuário
print('-----------------------------------------------')
print('Verifique o antecessor e sucessor de um número!')
print('-----------------------------------------------')

#Leitura de dados + Verificação de possíveis erros
while True:
    try:
        numero = int(input('Digite um número inteiro: '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números inteiros.')

# Exibição de resultados
print(f'Seu antecessor\033[33m {numero - 1}\033[m e seu sucessor \033[33m{numero + 1}\033[m')
