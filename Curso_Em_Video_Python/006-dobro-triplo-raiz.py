# Crie um algoritmo que leia um número
# e mostre o seu dobro, triplo e raiz quadrada.

print('-----------------------------------------------------')
print('Calcule o dobro, triplo e raiz quadrada de um número!')
print('-----------------------------------------------------')

# Leitura de dados + Verificação de possíveis erros
while True:
    try:
        numero = float(input('Digite um número: '))
        break
    except ValueError:
        print('Valor inválido! Digite apenas números inteiros.')

# Exibição de resultados
print(f'O dobro é:\033[33m {numero * 2:.2f} \033[m' # Deixar apenas com duas casas depois da virgula.
      f'\n O triplo é:\033[33m {numero * 3:.2f} \033[m'
      f'\n A Raiz quadrada é:\033[33m {numero ** 0.5:.2f} \033[m') # Raiz quadrada de um número é
# o mesmo que elevar esse número à potência ½.


