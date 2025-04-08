#1. Escreva um programa que peça ao usuário uma letra
#2. imprima se é uma vogal ou consoante.

#Leitura de dados
letra = (input('Digite uma letra: ')).strip().upper()[0]

#Correção acentuação - prevenção de erros
letra = letra.replace('Á', 'A')
letra = letra.replace('À', 'A')
letra = letra.replace('Â', 'A')
letra = letra.replace('Ã', 'A')
letra = letra.replace('É', 'E')
letra = letra.replace('Ê', 'E')
letra = letra.replace('Í', 'I')
letra = letra.replace('Ô', 'O')
letra = letra.replace('Ó', 'O')
letra = letra.replace('Õ', 'O')
letra = letra.replace('Ú', 'U')
letra = letra.replace('Ü', 'U')

#2.1 Condicional + Retorno de informações
if (letra == 'A') or (letra == 'E') or (letra == 'I') or (letra == 'O') or (letra == 'U'):
    print('Você digitou uma vogal')
else:
    print('Você digitou uma consoante')

#2.2
if letra in 'AEIOU':
    print('Você digitou uma vogal')
else:
    print('Você digitou uma consoante')

#2.3 Condicional + Retorno de informações
if (letra == 'A'):
    print('Você digitou uma vogal')
elif (letra == 'E'):
    print('Você digitou uma vogal')
elif (letra == 'I'):
    print('Você digitou uma vogal')
elif (letra == 'O'):
    print('Você digitou uma vogal')
elif (letra == 'U'):
    print('Você digitou uma vogal')
else:
    print('Você digitou uma consoante')
