# Faça o algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto

print('--------------------------------------')
print('CALCULO DE DESCONTO 5% EM UM PRODUTO. ')
print('--------------------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        preco = float(input('Quanto custa este produto: R$ '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números.')

# Exibição de resultados
print(f'O novo preço deste produto com desconto de 5% é:\033[33m R${preco * 0.95:.2f}')