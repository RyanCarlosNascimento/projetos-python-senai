# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

# Pede para o usuário digitar algo
entrada = input('Digite algo: ')

# Mostra o tipo primitivo do que foi digitado
print('O tipo primitivo desse valor é:', type(entrada))

# Mostra outras informações
print('Só tem espaços?', entrada.isspace())
print('É um número?', entrada.isnumeric())
print('É alfabético?', entrada.isalpha())
print('É alfanumérico?', entrada.isalnum())
print('Está em maiúsculas?', entrada.isupper())
print('Está em minúsculas?', entrada.islower())
print('Está capitalizada (primeira maiúscula)?', entrada.istitle())