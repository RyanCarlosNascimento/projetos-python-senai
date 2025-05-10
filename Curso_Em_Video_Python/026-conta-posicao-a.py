# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
# em que posição ela aparece a primeira vez
# e em que posição ela aparece a última vez.

# Leitura de dados
frase = input('Digite uma frase: ').strip().upper()

# Exibição de resultados
print(f'A quantidade de A(s) na frase é(são):\033[33m {frase.count('A')} \033[m'
      f'\nEle aparece pela primeira vez na posição:\033[33m {frase.find('A') + 1} \033[m'
      f'\nE aparece pela última vez na posição:\033[33m {frase.rfind('A') - 1} \033[m')

